
from ..serializers.serializers_car_engine_type import Car_EngineTypeSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_engine_type import Car_EngineType
from rest_framework.response import Response


class CustomLimitOffsetPaginationEngineType(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################
# class Car_EngineTypeAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_EngineTypeViewSet(viewsets.ModelViewSet):
    queryset = Car_EngineType.objects.all()
    serializer_class = Car_EngineTypeSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_engine_type']

    pagination_class = CustomLimitOffsetPaginationEngineType  # определенная пагинация


class Car_EngineTypeCreate(generics.ListCreateAPIView):
    queryset = Car_EngineType.objects.all()
    serializer_class = Car_EngineTypeSerializer


class Car_EngineTypeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_EngineType.objects.all()
    serializer_class = Car_EngineTypeSerializer
