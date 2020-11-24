from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name       = models.CharField(max_length=150, default='')
    surname    = models.CharField(max_length=150, default='')
    pseudonyme = models.CharField(max_length=150, default='')
    password   = models.CharField(max_length=150, default='')

class Book(models.Model):
     title       = models.TextField(default='')
     description = models.TextField(default='')    
     author      = models.TextField(default='')    
     price       = models.FloatField(default=0)
     image_link  = models.CharField(max_length=300, default='')
     
