from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ..serializers.serializers_car import CarSerializer
from rest_framework import viewsets, filters, generics, status
from ..permissions import AllForAdminOtherReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car import Car
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.response import Response


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 40
    max_limit = 100

    def get_paginated_response(self, data):
        return Response(data)

##################################################
# class CarAPIListPagination(PageNumberPagination):  # определенная пагинация
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllForAdminOtherReadOnly, )  # IsAuthenticatedOrReadOnly -- права доступа только по чтению
    #filter_backends = [filters.SearchFilter]  # фильтрация данных по поиску
    filter_backends = [filters.OrderingFilter]  # фильтрация данных по сортировке в виде http://127.0.0.1:8000/api/player/?ordering=price_usd

    # поиск осуществляется в виде http://127.0.0.1:8000/api/player/?search=2020
    search_fields = ['id', 'car_title', 'car_model', 'car_generation', 'car_vin', 'main_car_image', 'car_images',
                    'year', 'transmission', 'engine', 'fuel', 'car_body', 'car_drive', 'car_color', 'horse_power',
                    'consumption', 'mileage', 'price_byn', 'price_usd', 'city', 'description', 'car_options',
                    'http_link']

    pagination_class = CustomLimitOffsetPagination  # определенная пагинация


class CarCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def add_car(self, request):  # получение данных из запроса
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Ваше объявление о продаже авто успешно добавлено!!'
            }
            return Response({**serializer.data, **response_data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


@method_decorator(csrf_exempt, name='dispatch')
class CarView(View):
    def post(self, request):
        return HttpResponse('POST request processed successfully')

    def get(self, request):
        return HttpResponse('Get request processed successfully')


