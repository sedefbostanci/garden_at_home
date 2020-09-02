from django.conf.urls import url
from .views import DeviceSlotsAll,DeviceSlotsUpdate,delete_deviceSpots

urlpatterns = [
    url(r'^deviceSlots_add/', DeviceSlotsAll),
    url(r'^deviceSlotsUpdate/', DeviceSlotsUpdate),
    url(r'^deviceSlots_get/', DeviceSlotsAll),
    url(r'^delete_deviceSpots/(?P<pk>[0-9]+)/(?P<spot_Number>[0-9]+)$',delete_deviceSpots, name='delete_deviceSpots'),

]
