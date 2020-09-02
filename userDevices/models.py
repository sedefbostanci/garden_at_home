from django.db import models

# Create your models here.
class UserDevices(models.Model):
    user = models.ForeignKey('users_new.CustomUser', on_delete=models.CASCADE)
    device = models.ForeignKey('device.Device', on_delete=models.CASCADE)
    connection_Date=models.CharField(max_length=55, blank=True,
                                  null=True)
    wifi_name=models.CharField(max_length=55, blank=True,
                                  null=True)
    wifi_password=models.CharField( max_length=255, blank=True,
                                  null=True)

    device_WaterLevel=models.CharField( max_length=5, blank=True,
                                  null=True)
    device_Name=models.CharField(max_length=55,blank=True,
                                  null=True)
