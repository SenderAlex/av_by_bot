
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_drive import Car_DriveViewSet


router10 = routers.DefaultRouter()
router10.register('car_drives', Car_DriveViewSet)

urlpatterns = [
    path('', include(router10.urls)),
]
