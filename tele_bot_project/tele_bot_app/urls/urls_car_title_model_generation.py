
from django.urls import path, include
from rest_framework import routers
from ..views.views_car_title_model_generation import (Car_TitleViewSet, Car_TitleCreate,
                    Car_TitleRetrieveUpdateDelete, Car_ModelViewSet, Car_ModelCreate, Car_ModelRetrieveUpdateDelete,
                    Car_GenerationViewSet, Car_GenerationCreate, Car_GenerationRetrieveUpdateDelete,
                                                      get_car_models_by_title, get_car_generations_by_model)


router2 = routers.DefaultRouter()
router2.register('car_titles', Car_TitleViewSet)

router3 = routers.DefaultRouter()
router3.register('car_model', Car_ModelViewSet)  # разобраться почему 'car_model(s)'

router4 = routers.DefaultRouter()
router4.register('car_generation', Car_GenerationViewSet)  # разобраться почему 'car_generation(s)'


urlpatterns = [
    path('', include(router2.urls)),
    path('', include(router3.urls)),
    path('', include(router4.urls)),
    path('car_title-create/', Car_TitleCreate.as_view(), name='car_title-create'),
    path('car_title-create/<int:pk>/', Car_TitleRetrieveUpdateDelete.as_view(), name='car_title-details'),
    path('car_model-create/', Car_ModelCreate.as_view(), name='car_model-create'),
    path('car_model-create/<int:pk>/', Car_ModelRetrieveUpdateDelete.as_view(), name='car_model-details'),
    path('car_generation-create/', Car_GenerationCreate.as_view(), name='car_generation-create'),
    path('car_generation-create/<int:pk>/', Car_GenerationRetrieveUpdateDelete.as_view(), name='car_generation-details'),
    path('car_models/car_models_by_title/', get_car_models_by_title), #?????
    path('car_generations/car_generations_by_model/', get_car_generations_by_model),
]
