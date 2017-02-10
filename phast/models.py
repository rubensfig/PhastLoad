from __future__ import unicode_literals

from django.db import models

class Upload(models.Model):
    model = models.FileField(upload_to = 'uploads', blank=False, null=False)
