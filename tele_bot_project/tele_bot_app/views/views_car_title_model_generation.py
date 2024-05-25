
from django.db.models import Q
from ..serializers.serializers_car_title_model_generation import (Car_TitleSerializer, Car_ModelSerializer,
                                                                  Car_GenerationSerializer)
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_title_model_generation import Car_Title, Car_Model, Car_Generation
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response


class CustomLimitOffsetPaginationTitle(LimitOffsetPagination):
    default_limit = 200
    max_limit = 200

    def get_paginated_response(self, data):
        return Response(data)
##################################


# class Car_TitleAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 140
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_TitleViewSet(viewsets.ModelViewSet):
    queryset = Car_Title.objects.all()
    serializer_class = Car_TitleSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_title']

    pagination_class = CustomLimitOffsetPaginationTitle  # определенная пагинация


class Car_TitleCreate(generics.ListCreateAPIView):
    queryset = Car_Title.objects.all()
    serializer_class = Car_TitleSerializer


class Car_TitleRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Title.objects.all()
    serializer_class = Car_TitleSerializer


##################################
class CustomLimitOffsetPaginationModel(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    # def get_paginated_response(self, data):
    #     return Response(data)
##################################

# class Car_ModelAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_ModelViewSet(viewsets.ModelViewSet):
    queryset = Car_Model.objects.all()
    serializer_class = Car_ModelSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd
    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_model', 'car_title_id']

    pagination_class = CustomLimitOffsetPaginationModel  # определенная пагинация


def get_car_models_by_title(request):
    car_title = request.GET.get('car_title')
    if car_title:
        car_models = Car_Model.objects.select_related('car_title_id').filter(car_title_id__car_title=car_title)
        if car_models.exists():
            car_models_data = [
                {
                    'id': car_model.id,
                    'car_model': car_model.car_model,
                    'car_title_id_id': car_model.car_title_id_id
                }
                for car_model in car_models
            ]
            return JsonResponse(car_models_data, safe=False)
        else:
            return JsonResponse({'error': 'Car models not found'}, status=404)
    else:
        return JsonResponse({'error': 'Please provide a car title'}, status=400)


class Car_ModelCreate(generics.ListCreateAPIView):
    queryset = Car_Model.objects.all()
    serializer_class = Car_ModelSerializer


class Car_ModelRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Model.objects.all()
    serializer_class = Car_ModelSerializer


##################################
class CustomLimitOffsetPaginationGeneration(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################

# class Car_GenerationAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_GenerationViewSet(viewsets.ModelViewSet):
    queryset = Car_Generation.objects.all()
    serializer_class = Car_GenerationSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_generation', 'car_model_id']

    pagination_class = CustomLimitOffsetPaginationGeneration  # определенная пагинация


def get_car_generations_by_model(request):
    car_model = request.GET.get('car_model')
    if car_model:
        car_generations = Car_Generation.objects.select_related('car_model_id').filter(car_model_id__car_model=car_model)
        if car_generations.exists():
            car_generations_data = [
                {
                    'id': car_generation.id,
                    'car_generation': car_generation.car_generation,
                    'car_model_id_id': car_generation.car_model_id_id
                }
                for car_generation in car_generations
            ]
            return JsonResponse(car_generations_data, safe=False)
        else:
            return JsonResponse({'error': 'Car models not found'}, status=404)
    else:
        return JsonResponse({'error': 'Please provide a car title'}, status=400)


class Car_GenerationCreate(generics.ListCreateAPIView):
    queryset = Car_Generation.objects.all()
    serializer_class = Car_GenerationSerializer


class Car_GenerationRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Generation.objects.all()
    serializer_class = Car_GenerationSerializer


