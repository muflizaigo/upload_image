from django.db import models

class UploadedImage(models.Model):
    image = models.FileField(upload_to='images/')
   
