
from ..serializers.serializers_car_engine import Car_EngineSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_engine import Car_Engine
from rest_framework.response import Response


class CustomLimitOffsetPaginationEngine(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################
# class Car_EngineAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_EngineViewSet(viewsets.ModelViewSet):
    queryset = Car_Engine.objects.all()
    serializer_class = Car_EngineSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_engine']

    pagination_class = CustomLimitOffsetPaginationEngine  # определенная пагинация


class Car_EngineCreate(generics.ListCreateAPIView):
    queryset = Car_Engine.objects.all()
    serializer_class = Car_EngineSerializer


class Car_EngineRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Engine.objects.all()
    serializer_class = Car_EngineSerializer