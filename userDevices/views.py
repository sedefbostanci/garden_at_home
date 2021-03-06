from django.shortcuts import render
from userDevices.models import UserDevices
from .serializers import UserDeviceAddSerializer,waterLevel
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
User = get_user_model()


@api_view(['POST',])
@permission_classes([AllowAny])
def add_device_user(request):

    serializer = UserDeviceAddSerializer(data=request.data)
    data={}
    if serializer.is_valid():

        userDevice = serializer.save()
        data['uDevice_ID']=userDevice.id
        return Response(data=data,status=status.HTTP_200_OK)
    else:
        data=serializer.errors
        return Response(data,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE',])
@permission_classes([AllowAny])

def delete_userDevice(request,pk):

    try:
        userDevice = UserDevices.objects.get(pk=pk)
        userDevice.delete()
        return JsonResponse({'message': 'userDevice was deleted successfully!'},status=status.HTTP_200_OK)
    except UserDevices.DoesNotExist:
        return JsonResponse({'message': 'The userDevice does not exist'}, status=status.HTTP_404_NOT_FOUND)


class UserDevicesAPIView(generics.ListAPIView):

    permission_classes = [AllowAny, ]

    def get(self,request):

        uid = self.request.GET.get('user_ID', None)
        if uid is not None:

            try:
                user = User.objects.get(id=uid)
                devices=UserDevices.objects.filter(user=user).all().values()

                b=list(devices)
                return JsonResponse(b,safe=False)
            except User.DoesNotExist:
                return JsonResponse({'message': 'This user does not exist'}, status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
@permission_classes([AllowAny])

def update_WaterLevel(request,pk,recent_WaterLevel):

    try:
        userDevice = UserDevices.objects.get(pk=pk)
        print(userDevice.device_WaterLevel)
        userDevice.__setattr__("device_WaterLevel", recent_WaterLevel)
        userDevice.save()
        print(userDevice.device_WaterLevel)
        return JsonResponse({'message': 'userDevice water level updated successfully!'},status=status.HTTP_200_OK)
    except UserDevices.DoesNotExist:
        return JsonResponse({'message': 'The userDevice does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST',])
@permission_classes([AllowAny])

def update_WaterLevel2(request):

    try:
        uid=request.GET.get('pk', None)
        recent_WaterLevel=request.GET.get('recent_WaterLevel', None)
        print(uid)
        print(recent_WaterLevel)
        print("aaaaaaaa")
        userDevice = UserDevices.objects.get(pk=uid)
        print(userDevice.device_WaterLevel)
        userDevice.__setattr__("device_WaterLevel", recent_WaterLevel)
        userDevice.save()
        print(userDevice.device_WaterLevel)
        return JsonResponse({'message': 'userDevice water level updated successfully!'},status=status.HTTP_200_OK)
    except UserDevices.DoesNotExist:
        return JsonResponse({'message': 'The userDevice does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST',])
@permission_classes([AllowAny])

def update_WaterLevel3(request):

    print("dgşfgkkşg")
    x=json.loads(request.body)
    print(x)

    return JsonResponse({'message': 'successfully!'},status=status.HTTP_200_OK)
