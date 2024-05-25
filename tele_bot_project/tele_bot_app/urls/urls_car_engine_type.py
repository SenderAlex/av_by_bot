
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_engine_type import Car_EngineTypeViewSet


router9 = routers.DefaultRouter()
router9.register('car_engine_types', Car_EngineTypeViewSet)

urlpatterns = [
    path('', include(router9.urls)),
]
