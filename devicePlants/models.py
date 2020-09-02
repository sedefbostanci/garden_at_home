from django.db import models

# Create your models here.
class DevicePlants(models.Model):
    uDevice_ID = models.ForeignKey('userDevices.UserDevices', on_delete=models.CASCADE)
    spot_1_ID=models.IntegerField(blank=True,
                                  null=True)
    spot_2_ID=models.IntegerField(blank=True,
                                  null=True)
    spot_3_ID=models.IntegerField(blank=True,
                                  null=True)
    spot_4_ID=models.IntegerField(blank=True,
                                  null=True)
    spot_5_ID=models.IntegerField(blank=True,
                                  null=True)
    spot_6_ID=models.IntegerField(blank=True,
                                  null=True)
    currentSpotSize=models.IntegerField(blank=True,
                                  null=True)
    spot_1_Name=models.CharField(max_length=55,blank=True, null=True)
    spot_2_Name=models.CharField(max_length=55,blank=True,null=True)
    spot_3_Name=models.CharField(max_length=55,blank=True, null=True)
    spot_4_Name=models.CharField(max_length=55,blank=True,null=True)
    spot_5_Name=models.CharField(max_length=55,blank=True,null=True)
    spot_6_Name=models.CharField(max_length=55,blank=True,null=True)
