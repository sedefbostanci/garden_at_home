from django.urls import path
from django.conf.urls import url

from .views import add_device_user,UserDevicesAPIView,delete_userDevice,update_WaterLevel,update_WaterLevel2

urlpatterns = [

    path('add_device_user',add_device_user,name="add_device_user"),
    path('get_userDevice/', UserDevicesAPIView.as_view(), name='userDevicesall'),
    url(r'^delete_userDevice/(?P<pk>[0-9]+)$',delete_userDevice, name='delete_device_user'),
    url(r'^update_WaterLevel/(?P<pk>[0-9]+)/(?P<recent_WaterLevel>\d+\.\d+)$',update_WaterLevel, name='update_WaterLevel'),
    url(r'^update_WaterLevel/',update_WaterLevel2, name='update_WaterLevel'),
]
