# users/urls.py

from rest_framework import routers
from django.urls import path, include
from .views import AuthViewSet,get_all,get_statics
from django.conf.urls import url
router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^get_all/(?P<pk>[0-9]+)$',get_all, name='get_all'),
    url(r'^get_statics/(?P<pk>[0-9]+)$',get_statics, name='get_statics'),
]
