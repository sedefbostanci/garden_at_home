from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):

    device_type = serializers.CharField(max_length=50)
    device_picture = serializers.CharField(max_length=200)
    device_description = serializers.CharField(max_length=250)

    class Meta:
        model=Device
        fields="__all__"

    def save(self):
        device=Device(device_type=self.validated_data['device_type'],device_picture=self.validated_data['device_picture'],device_description=self.validated_data['device_description'])
        device.save()
        return device
