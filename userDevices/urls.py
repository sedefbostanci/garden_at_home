from django.urls import path
from django.conf.urls import url

from .views import add_device_user,UserDevicesAPIView,delete_userDevice

urlpatterns = [

    path('add_device_user',add_device_user,name="add_device_user"),
    path('get_userDevice/', UserDevicesAPIView.as_view(), name='userDevicesall'),
    url(r'^delete_userDevice/(?P<pk>[0-9]+)$',delete_userDevice, name='delete_device_user'),

]
