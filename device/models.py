from django.db import models

class Device(models.Model):

    device_type = models.CharField(max_length=50)
    device_picture = models.URLField(max_length=200)
    device_description = models.CharField(max_length=250)

    
