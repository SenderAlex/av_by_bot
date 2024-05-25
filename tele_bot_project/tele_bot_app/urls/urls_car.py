
from django.urls import path, include
from rest_framework import routers
from ..views.views_car import CarViewSet, CarCreate, CarRetrieveUpdateDelete, CarView
from ..views.views_filtered_cars import get_filtered_cars


router = routers.DefaultRouter()
router.register('api/cars', CarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/car-create/', CarCreate.as_view(), name='car-create'),
    path('car-create/<int:pk>/', CarRetrieveUpdateDelete.as_view(), name='car-details'),
    path('Car/<int:pk>/', CarView.as_view(), name='carview'),
    path('api/filtered_cars/', get_filtered_cars),
]
