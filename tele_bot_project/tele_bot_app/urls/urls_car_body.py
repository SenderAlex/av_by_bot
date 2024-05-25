
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_body import Car_BodyViewSet


router8 = routers.DefaultRouter()
router8.register('car_bodies', Car_BodyViewSet)

urlpatterns = [
    path('', include(router8.urls)),
]
