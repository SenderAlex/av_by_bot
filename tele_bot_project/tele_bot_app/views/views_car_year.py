
from ..serializers.serializers_car_year import Car_YearSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_year import Car_Year
from rest_framework.response import Response


class CustomLimitOffsetPaginationYear(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################
# class Car_YearAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 120
#     page_size_query_param = 'page_size'
#     max_page_size = 120

class Car_YearViewSet(viewsets.ModelViewSet):
    queryset = Car_Year.objects.all()
    serializer_class = Car_YearSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_year']

    pagination_class = CustomLimitOffsetPaginationYear  # определенная пагинация


class Car_YearCreate(generics.ListCreateAPIView):
    queryset = Car_Year.objects.all()
    serializer_class = Car_YearSerializer


class Car_YearRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Year.objects.all()
    serializer_class = Car_YearSerializer


