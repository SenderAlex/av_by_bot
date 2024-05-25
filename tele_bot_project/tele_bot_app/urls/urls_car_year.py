
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_year import Car_YearViewSet


router5 = routers.DefaultRouter()
router5.register('car_years', Car_YearViewSet)


urlpatterns = [
    path('', include(router5.urls)),
]
