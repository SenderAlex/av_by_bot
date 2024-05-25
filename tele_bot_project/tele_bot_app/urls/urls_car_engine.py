
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_engine import Car_EngineViewSet


router6 = routers.DefaultRouter()
router6.register('car_engines', Car_EngineViewSet)


urlpatterns = [
    path('', include(router6.urls)),
]
