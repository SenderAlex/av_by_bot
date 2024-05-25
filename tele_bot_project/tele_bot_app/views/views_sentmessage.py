
from ..serializers.serializers_sentmessage import SentMessageSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_sentmessage import SentMessage


class SentMessageAPIListPagination(PageNumberPagination):  # определенная пагинация
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class SentMessageViewSet(viewsets.ModelViewSet):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['telegram_id', 'message']

    pagination_class = SentMessageAPIListPagination  # определенная пагинация


class SentMessageCreate(generics.ListCreateAPIView):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer


class SentMessageRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = SentMessage.objects.all()
    serializer_class = SentMessageSerializer

