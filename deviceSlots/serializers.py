from rest_framework import serializers
from .models import DeviceSlots
from devicePlants.models import DevicePlants

class DeviceSlotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceSlots
        fields = ('id',
                  'devicePlants_ID',
                  'remaining_Time',
                  'starting_Date',
                  'plant_Name',
                  'avg_GrowTime',
                  'plant_Description',
                  'plant_Tips',
                  'device_Info')

        def save(self):

            try:
                print("save method")
                devicePlants=DevicePlants.objects.get(id=int(self.validated_data['devicePlants_ID']))

                spot=DeviceSlots(devicePlants_ID=devicePlants,remaining_Time=int(self.validated_data['remaining_Time']),
                                        starting_Date=self.validated_data['starting_Date'],plant_Name=self.validated_data['plant_Name'],
                                        avg_GrowTime=int(self.validated_data['avg_GrowTime']),plant_Description=self.validated_data['plant_Description']
                                        ,plant_Tips=self.validated_data['plant_Tips'],device_Info=self.validated_data['device_Info'])

                spot.save()
                return device
            except Exception as e:
                print(e)
