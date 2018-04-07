from django.db import models

# Create your models here.
class Beaches(models.Model): 

    BEACH_TYPES = (
        ('B', 'Beginner'),
        ('M', 'Medium'),
        ('A', 'Advanced'),
    )

    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=30)
    latX = models.DecimalField(max_length=30)
    latY = models.DecimalField(max_length=30)
    cond = models.CharField(max_length=30, choices=BEACH_TYPES)

class Users(models.Model):

    EXPERIENCE = (
        ('B', 'Beginner'),
        ('M', 'Medium'),
        ('A', 'Advanced'),
    )

    id = models.CharField(max_length=30, primary_key=True)
    exp = models.CharField(max_length=30, choices=EXPERIENCE)
