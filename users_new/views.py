from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db import connection
from . import serializers
from .utils import get_and_authenticate_user,create_user_account
from django.contrib.auth import get_user_model,login,logout
from django.http import JsonResponse

User = get_user_model()


#@csrf_exempt
class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]

    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'password_change': serializers.PasswordChangeSerializer,
        #'add_device_user': serializers.UserDeviceAddSerializer,

    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_and_authenticate_user(**serializer.validated_data)

        data = serializers.UserSerializer(user).data
        login(request,user)
        return Response(data=data,status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def register(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            user = create_user_account(**serializer.validated_data)
            data = serializers.AuthUserSerializer(user).data
            return Response(data=data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False)
    def password_change(self, request):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            try:
                user = User.objects.get(email=serializer.data.get("email"))
                token = Token.objects.get(key=serializer.data.get("token"))
                user_token=Token.objects.get(user=user)

                if(token != user_token):
                    return Response({"This user dont have permission"}, status=status.HTTP_400_BAD_REQUEST)
                else:

                    if not user.check_password(serializer.data.get("current_password")):

                            return Response({"current_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                        # set_password also hashes the password that the user will get
                    user.set_password(serializer.data.get("new_password"))
                    user.save()
                    return Response({'Password updated successfully'},status=status.HTTP_200_OK)

            except:
                return Response({"Password couldnt change"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_serializer_class(self):
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()

    def get_queryset(self) :
        user = self.request.user
        return User.objects.all()

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

@api_view(['POST',])
@permission_classes([AllowAny])

def get_all(request,pk):

    cursor = connection.cursor()

    try:
          cursor.execute("SELECT ud.device_Name,ds.* FROM users_new_customuser as u ,userDevices_userdevices as ud ,devicePlants_deviceplants as dp, deviceSlots_deviceslots as ds WHERE u.id= ud.user_id AND ud.id = dp.uDevice_ID_id AND dp.id = ds.devicePlants_ID_id AND u.id = %s",[pk])

          row = cursor.fetchall()

          return JsonResponse(row,safe=False)
    except Exception as e:
          cursor.close
          return Response({"it is not okey"}, status=status.HTTP_400_BAD_REQUEST)
