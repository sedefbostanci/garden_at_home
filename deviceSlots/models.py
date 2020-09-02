from django.db import models

# Create your models here.
class DeviceSlots(models.Model):
    devicePlants_ID = models.ForeignKey('devicePlants.DevicePlants', on_delete=models.CASCADE)

    remaining_Time=models.IntegerField(blank=True,
                                  null=True)
    starting_Date=models.CharField(max_length=55, blank=True,
                                  null=True)
    plant_Name=models.CharField(max_length=55, blank=True,
                                  null=True)
    avg_GrowTime=models.IntegerField(blank=True,
                                  null=True)
    plant_Description=models.TextField(blank=True,
                                  null=True)
    plant_Tips=models.TextField(blank=True,
                                  null=True)
    device_Info=models.CharField(max_length=55, blank=True,
                                  null=True)
