from django.contrib import admin
from .models import DevicePlants
@admin.register(DevicePlants)

class DeviceAdmin(admin.ModelAdmin):
    list_display=['id',
              'uDevice_ID',
              'spot_1_ID',
              'spot_2_ID',
              'spot_3_ID',
              'spot_4_ID',
              'spot_5_ID',
              'spot_6_ID',
              'currentSpotSize',
              'spot_1_Name',
              'spot_2_Name',
              'spot_3_Name',
              'spot_4_Name',
              'spot_5_Name',
              'spot_6_Name']

    class Meta:
        model=DevicePlants
# Register your models here.
