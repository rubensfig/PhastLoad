from django.db import models

# Create your models here.
class Users(models.Model): 
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)

class Files(models.Model):
    file_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
