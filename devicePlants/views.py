from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import DevicePlants
from userDevices.models import UserDevices
from .serializers import DevicePlantsSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.
@api_view(['POST','GET',])
@permission_classes([AllowAny])
def DevicePlantsAll(request):

    if request.method == 'POST':

        serializer = DevicePlantsSerializer(data=request.data)

        if serializer.is_valid():
            device=serializer.save()
            data={}
            print("dkdsklfsj")
            print(device.id)
            data["devicePlants_ID"]=device.id
            return JsonResponse(data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        uDevice_ID = request.query_params.get('uDevice_ID', None)

        if uDevice_ID is not None:
            try:
                devicePlants = DevicePlants.objects.filter(uDevice_ID_id=uDevice_ID)

                devicePlants_serializer = DevicePlantsSerializer(devicePlants, many=True)
                return JsonResponse(devicePlants_serializer.data, safe=False)

            except DevicePlants.DoesNotExist:
                return JsonResponse({'message': 'The devicePlants does not exist'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'message': 'wrong parameter'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE',])
@permission_classes([AllowAny])

def delete_devicePlants(request,pk):

    try:
        devicePlants = DevicePlants.objects.get(pk=pk)
        devicePlants.delete()
        return JsonResponse({'message': 'devicePlants was deleted successfully!'}, status=status.HTTP_200_OK)
    except UserDevices.DoesNotExist:
        return JsonResponse({'message': 'The devicePlants does not exist'}, status=status.HTTP_404_NOT_FOUND)
