
from rest_framework import serializers
from .models import UserDevices
from django.contrib.auth import get_user_model
from device.models import Device
User = get_user_model()

class UserDeviceAddSerializer(serializers.Serializer):

    user_ID = serializers.CharField()
    device_ID = serializers.CharField()
    connection_Date=serializers.CharField(max_length=55)
    wifi_name=serializers.CharField(max_length=55)
    wifi_password=serializers.CharField( max_length=255)
    device_WaterLevel=serializers.CharField()
    device_Name=serializers.CharField(max_length=55)

    class Meta:
         model = UserDevices
         fields ="__all__"

    def save(self):

        try:
            print("save method")
            device=Device.objects.get(id=int(self.validated_data['device_ID']))
            user=User.objects.get(id=int(self.validated_data['user_ID']))
            #device=Device.objects.get(id=self.validated_data['device_ID'])
            #user=User.objects.get(id=self.validated_data['user_ID'])
            print("user ve device alındı")
            print(user.email)
            print(device.device_type)

            userDevice=UserDevices(user=user,device=device,connection_Date=self.validated_data['connection_Date'],wifi_name=self.validated_data['wifi_name'],wifi_password=self.validated_data['wifi_password'],device_WaterLevel=self.validated_data['device_WaterLevel'],device_Name=self.validated_data['device_Name'])

            userDevice.save()
            return userDevice
        except Exception as e:
            print(e)
