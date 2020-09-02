from django.conf.urls import url
from .views import DevicePlantsAll,delete_devicePlants

urlpatterns = [
    url(r'^devicePlants_add/', DevicePlantsAll),
    url(r'^delete_devicePlants/(?P<pk>[0-9]+)$',delete_devicePlants, name='delete_devicePlants'),


]
