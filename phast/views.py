from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.db import connection, IntegrityError
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile, File

from functions import encrypt
from models import Upload
from forms import UploadFileForm

from random import randint
import json
import os
import fileEnc
import sys, traceback

class LegacyDatabase(object):
    cursor = None

    def __init__(self):
        try:
            self.cursor = connection.cursor()
        except Exception:
            print "Database is not configured"

    def query(self, query, param):
        if self.cursor:
            self.cursor.execute(query,param)
            return self.cursor

def dBGetExistingValue(dB, filename):

    sql_string = 'SELECT sessionid FROM draggable.files WHERE paths = (%s)'
    param = (filename,)

    res = dB.query(sql_string, param).fetchall()

    return res[0][0]

def dBconnection(dB, filename):

    sql_string = 'INSERT INTO draggable.files VALUES (%s, %s)'

    sessionid = randint(1000, 9999)
    param = (sessionid, filename)

    dB.query(sql_string, param)

    return sessionid

def dBgetFilename(dB, filename):
    sql_string = 'SELECT paths from draggable.files WHERE sessionid =(%s)'
    param = (filename,)

    res = dB.query(sql_string, param).fetchall()

    if len(res) == 0:
        return None
    else:
        return res[0][0]

def submit(dB, request):
    return dBgetFilename(dB, request.POST['fileId'])

def downloadFile(filename):
    path = '/home/rubinhus/Development/django/phastload/media/uploads/'
    fpath = os.path.join(path + filename)

    infile = open(fpath, 'rb+')

    outfile = decryptfile(infile)

    wrapper = FileWrapper(outfile)

    response = HttpResponse(wrapper, content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    response['X-Sendfile'] = smart_str(outfile)
    #response['Content-Length'] = os.path.getsize(outfile)
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response

def decryptfile(infile):
    out_file = ContentFile(None)

    fileEnc.decrypt(infile, out_file, 'password')

    return out_file

def encryptfile(filename, data):
    out_file = ContentFile(None)
    in_file = ContentFile(data, filename)

    fileEnc.encrypt(in_file, out_file, 'password')

    in_file.close()

    return out_file

def uploadFileEncrypted(filename, data):
    path = '/home/rubinhus/Development/django/phastload/media/uploads/'
    encr = encryptfile(filename, data)

    retValue = None

    try:
        default_storage.save(os.path.join(path + filename), encr)
        retValue = True
    except Exception:
        traceback.print_exc(file=sys.stdout)
        retValue = False

    encr.close()

    return retValue

def generateJSON(key, value):
    response_data = {}
    response_data[key] = value

    return dict(response_data)

def index(request):
    dB = LegacyDatabase()
    ints = None
    in_file = None
    out_file = None
    sess = None
    if request.POST:
        if "fileId" in request.POST:
            filename = submit(dB, request)
            if filename is None:
                sess = generateJSON("file", False)
                return JsonResponse(sess)

            here = downloadFile(filename)

            sess = generateJSON("file", True)

            return here
        else:
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                if not uploadFileEncrypted(request.FILES['file_upload'].name, request.FILES['file_upload'].read()):
                    return render(request, "main/index.html")
                try:
                    ints = dBconnection(dB, request.FILES['file_upload'].name)
                except IntegrityError:
                    ints = dBGetExistingValue(dB, request.FILES['file_upload'].name)

                sess = generateJSON("sessionid", ints)
                return render(request, "main/index.html")

    return render(request, "main/index.html", context=sess)
