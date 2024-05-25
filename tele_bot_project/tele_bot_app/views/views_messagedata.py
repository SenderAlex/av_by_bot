
from ..serializers.serializers_messagedata import MessageDataSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_messagedata import MessageData


class MessageDataAPIListPagination(PageNumberPagination):  # определенная пагинация
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class MessageDataViewSet(viewsets.ModelViewSet):
    queryset = MessageData.objects.all()
    serializer_class = MessageDataSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['telegram_id', 'first_name', 'last_name', 'phone_number', 'message']

    pagination_class = MessageDataAPIListPagination  # определенная пагинация


class MessageDataCreate(generics.ListCreateAPIView):
    queryset = MessageData.objects.all()
    serializer_class = MessageDataSerializer


class MessageDataRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = MessageData.objects.all()
    serializer_class = MessageDataSerializer


