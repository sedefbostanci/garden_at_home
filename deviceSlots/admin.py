from django.contrib import admin
from .models import DeviceSlots
@admin.register(DeviceSlots)

class DeviceAdmin(admin.ModelAdmin):
    list_display=["id","devicePlants_ID","plant_Name"]

    class Meta:
        model=DeviceSlots
# Register your models here.
