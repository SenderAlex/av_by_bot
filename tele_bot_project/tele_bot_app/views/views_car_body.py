
from ..serializers.serializers_car_body import Car_BodySerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_body import Car_Body
from rest_framework.response import Response


class CustomLimitOffsetPaginationBody(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################
# class Car_BodyAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_BodyViewSet(viewsets.ModelViewSet):
    queryset = Car_Body.objects.all()
    serializer_class = Car_BodySerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_body']

    pagination_class = CustomLimitOffsetPaginationBody  # определенная пагинация


class Car_BodyCreate(generics.ListCreateAPIView):
    queryset = Car_Body.objects.all()
    serializer_class = Car_BodySerializer


class Car_BodyRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Body.objects.all()
    serializer_class = Car_BodySerializer


