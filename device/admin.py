from django.contrib import admin

from .models import Device
@admin.register(Device)

class DeviceAdmin(admin.ModelAdmin):
    list_display=["id","device_type","device_description","device_picture"]

    class Meta:
        model=Device
# Register your models here.
