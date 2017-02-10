from models import Upload
from django import forms

class UploadFileForm(forms.Form):
    file_upload = Upload
    fields = ('model',)
