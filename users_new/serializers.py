#from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth import password_validation
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email', 'is_active', 'is_staff','auth_token')
         read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass


class UserRegisterSerializer(serializers.ModelSerializer):
    """
        A user serializer for registering the user
    """

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')


    def validate_email(self, value):

        user = User.objects.filter(email=value)
        return BaseUserManager.normalize_email(value)

class PasswordChangeSerializer(serializers.Serializer):

    model = User

    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    token = serializers.CharField(required=True)
    email = serializers.CharField(required=True)



class UserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()

    class Meta:
         model = User
         fields = ('id', 'email','first_name','auth_token')
         read_only_fields = ('id', 'is_active', 'is_staff')

    def get_auth_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key

"""class UserDeviceAddSerializer(serializers.Serializer):

    class Meta:
         model = UserDevices
         fields ="__all__"

    def save(self):
        device=Device.objects.get(id=self.validated_data['device'])
        user=User.objects.get(id=self.validated_data['user'])
        userDevice=UserDevices(user=user,device=device,connection_date=self.validated_data['connection_date'],wifi_name=self.validated_data['wifi_name'],wifi_password=self.validated_data['wifi_password'],device_water_level=self.validated_data['device_water_level'])
        userDevice.save()
        return userDevice"""
