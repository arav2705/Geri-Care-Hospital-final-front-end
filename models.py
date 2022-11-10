import email
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class test(models.Model):
    firstname = models.CharField(max_length=30)
    secondname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    medhistory = models.CharField(max_length=100)
    concerns = models.CharField(max_length=100)
