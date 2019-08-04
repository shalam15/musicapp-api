# from django.conf.urls import urls
from django.urls import path, include
from . import views 
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('music', views.MusicView)

urlpatterns = [
    path('', include(router.urls))
]
