
from ..serializers.serializers_car_transmission import Car_TransmissionSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car_transmission import Car_Transmission
from rest_framework.response import Response


class CustomLimitOffsetPaginationTransmission(LimitOffsetPagination):
    default_limit = 140
    max_limit = 140

    def get_paginated_response(self, data):
        return Response(data)
##################################
# class Car_TransmissionAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class Car_TransmissionViewSet(viewsets.ModelViewSet):
    queryset = Car_Transmission.objects.all()
    serializer_class = Car_TransmissionSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_transmission']

    pagination_class = CustomLimitOffsetPaginationTransmission  # определенная пагинация


class Car_TransmissionCreate(generics.ListCreateAPIView):
    queryset = Car_Transmission.objects.all()
    serializer_class = Car_TransmissionSerializer


class Car_TransmissionRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car_Transmission.objects.all()
    serializer_class = Car_TransmissionSerializer
