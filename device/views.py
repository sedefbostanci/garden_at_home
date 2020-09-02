from django.shortcuts import render
from device.models import Device
from .serializers import DeviceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http.response import JsonResponse
# Create your views here.
@api_view(['POST',])
@permission_classes([AllowAny])

def DeviceRegister(request):

    if request.method=='POST':

        serializer=DeviceSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            device=serializer.save()
            data['device_id'] = device.id
            return Response(data,status=status.HTTP_200_OK)
        else:
            data=serializer.errors

            return Response(data,status=status.HTTP_400_BAD_REQUEST)

class DeviceAPIView(APIView):

    permission_classes = [AllowAny, ]
    def get(self,request):
        devices=Device.objects.all()
        serializer=DeviceSerializer(devices,many=True)

        return Response(serializer.data)

@api_view(['DELETE',])
@permission_classes([AllowAny])

def delete_Device(request,pk):

    try:
        device = Device.objects.get(pk=pk)
        device.delete()
        return JsonResponse({'message': 'device was deleted successfully!'}, status=status.HTTP_200_OK)
    except Device.DoesNotExist:
        return JsonResponse({'message': 'The device does not exist'}, status=status.HTTP_404_NOT_FOUND)
