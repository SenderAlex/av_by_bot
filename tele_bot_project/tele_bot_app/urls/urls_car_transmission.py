
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_transmission import Car_TransmissionViewSet


router7 = routers.DefaultRouter()
router7.register('car_transmissions', Car_TransmissionViewSet)


urlpatterns = [
    path('', include(router7.urls)),
]
