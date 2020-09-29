from django.db import models
import os

# Create your models here.

class Photo(models.Model):
     
     title = models.CharField(max_length=100)
     description = models.CharField(max_length=100)
     image = models.ImageField("Photo")
     oriLink = models.CharField("Original Link", max_length=100)
     
     def __str__(self):
         return self.title
    
     def filename(self):
        return os.path.basename(self.image.name)