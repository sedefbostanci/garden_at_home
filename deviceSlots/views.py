from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import DeviceSlots
from devicePlants.models import DevicePlants
from .serializers import DeviceSlotsSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.forms.models import model_to_dict
from rest_framework.response import Response
# Create your views here.

@api_view(['POST','GET',])
@permission_classes([AllowAny])
def DeviceSlotsAll(request):

    if request.method == 'POST':

        serializer = DeviceSlotsSerializer(data=request.data)
        print("fgkfdkgjgkdlgdj")
        if serializer.is_valid():

            spot=serializer.save()
            data={}
            data["spot_ID"]=spot.id

            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        serializer = DeviceSlotsSerializer(data=request.data)
        spot_ID = request.query_params.get('spot_ID', None)

        if spot_ID is not None:
            try:
                deviceSlots = DeviceSlots.objects.filter(id=spot_ID)

                deviceSlots_serializer = DeviceSlotsSerializer(deviceSlots, many=True)
                return JsonResponse(deviceSlots_serializer.data, safe=False)

            except DeviceSlots.DoesNotExist:
                return JsonResponse({'message': 'The deviceSlots does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'wrong parameter'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST','GET',])
@permission_classes([AllowAny])
def DeviceSlotsUpdate(request):

    if request.method == 'POST':

        serializer = DeviceSlotsSerializer(data=request.data)
        spot_Number = request.query_params.get('spot_Number', None)
        spot_ID = request.query_params.get('spot_ID', None)
        spot_Name = request.query_params.get('spot_Name', None)

        if spot_Number and spot_ID and spot_Name is not None:
            try:
                deviceSlots = DeviceSlots.objects.get(id=spot_ID)

                devicePlant=deviceSlots.devicePlants_ID
                which_spotID="spot"+"_"+str(spot_Number)+"_"+"ID"
                which_spotName="spot"+"_"+str(spot_Number)+"_"+"Name"
                #field_name = which_spotID

                devicePlant.__setattr__(which_spotID, spot_ID)
                devicePlant.__setattr__(which_spotName, spot_Name)
                devicePlant.save()
                print(devicePlant.spot_1_ID)

                return Response(status=status.HTTP_200_OK)

            except DeviceSlots.DoesNotExist:
                return JsonResponse({'message': 'The deviceSlots does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'wrong parameter'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE',])
@permission_classes([AllowAny])

def delete_deviceSpots(request,pk,spot_Number):

    try:
        deviceSlots = DeviceSlots.objects.get(pk=pk)

        devicePlant=deviceSlots.devicePlants_ID
        print(spot_Number)

        which_spotID="spot"+"_"+str(spot_Number)+"_"+"ID"
        which_spotName="spot"+"_"+str(spot_Number)+"_"+"Name"

        devicePlant.__setattr__(which_spotID, 0)
        devicePlant.__setattr__(which_spotName, "null")
        devicePlant.save()
        deviceSlots.delete()
        return JsonResponse({'message': 'deviceSpot was deleted successfully!'}, status=status.HTTP_200_OK)

    except DeviceSlots.DoesNotExist:
        return JsonResponse({'message': 'The deviceSpot does not exist'}, status=status.HTTP_404_NOT_FOUND)
