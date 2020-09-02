from django.contrib import admin
from .models import UserDevices
@admin.register(UserDevices)

class DeviceAdmin(admin.ModelAdmin):
    list_display=["id","user","device","connection_Date","device_Name"]

    class Meta:
        model=UserDevices
# Register your models here.
