from rest_framework import serializers
from .models import DevicePlants
from userDevices.models import UserDevices

class DevicePlantsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevicePlants
        fields = ('id',
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
                  'spot_6_Name',)

        def save(self):

            try:
                print("save method")
                userDevice=UserDevices.objects.get(id=int(self.validated_data['uDevice_ID']))

                device=DevicePlants(uDevice_ID=userDevice,spot_1_ID=int(self.validated_data['spot_1_ID']),
                                        spot_2_ID=int(self.validated_data['spot_2_ID']),spot_3_ID=int(self.validated_data['spot_3_ID']),
                                        spot_4_ID=int(self.validated_data['spot_4_ID']),spot_5_ID=int(self.validated_data['spot_5_ID']),
                                        spot_6_ID=int(self.validated_data['spot_6_ID']),currentSpotSize=int(self.validated_data['currentSpotSize']),
                                        spot_1_Name=self.validated_data['spot_1_Name'],spot_2_Name=self.validated_data['spot_2_Name'],
                                        spot_3_Name=self.validated_data['spot_3_Name'],spot_4_Name=self.validated_data['spot_4_Name']
                                        ,spot_5_Name=self.validated_data['spot_5_Name'],spot_6_Name=self.validated_data['spot_6_Name'])

                device.save()
                return device
            except Exception as e:
                print(e)
