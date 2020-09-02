from django.urls import path
from .views import DeviceRegister,DeviceAPIView,delete_Device
from django.conf.urls import url

urlpatterns = [

    path('adddevice_api',DeviceRegister,name="add_device"),
    path('get_all_devices_api',DeviceAPIView.as_view(),name="get_all_devices"),
    url(r'^delete_Device/(?P<pk>[0-9]+)',delete_Device, name='delete_Device'),

]
