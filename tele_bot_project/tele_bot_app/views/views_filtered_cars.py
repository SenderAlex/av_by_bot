
from ..serializers.serializers_car import CarSerializer
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from ..models.models_car import Car
from rest_framework.decorators import api_view


class PaginationFilteredCars(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100

    # def get_paginated_response(self, data):
    #     return Response(data)

@api_view(['GET'])
def get_filtered_cars(request):
    car_title = request.GET.get('car_title')
    car_model = request.GET.get('car_model')
    car_generation = request.GET.get('car_generation')
    car_year_from = request.GET.get('year_from')
    car_year_to = request.GET.get('year_to')
    car_price_from = request.GET.get('price_from')
    car_price_to = request.GET.get('price_to')
    car_engine_from = request.GET.get('engine_from')
    car_engine_to = request.GET.get('engine_to')
    car_transmission = request.GET.get('car_transmission')
    car_body = request.GET.get('car_body')
    car_fuel = request.GET.get('car_engine_type')
    car_drive = request.GET.get('car_drive')
    currency = request.GET.get('currency')

    queryset = Car.objects.all()

    if car_title:
        queryset = queryset.filter(car_title=car_title)

    if car_model:
        queryset = queryset.filter(car_model=car_model)

    if car_generation:
        car_generation = car_generation.split(',')[0]
        queryset = queryset.filter(car_generation=car_generation)

    if car_year_from and car_year_to:
        queryset = queryset.filter(year__range=(car_year_from, car_year_to))
    elif car_year_from:
        queryset = queryset.filter(year__gte=car_year_from)
    elif car_year_to:
        queryset = queryset.filter(year__lte=car_year_to)

    if currency == 'BYN':
        if car_price_from and car_price_to:
            queryset = queryset.filter(price_byn__range=(car_price_from, car_price_to))
        elif car_price_from:
            queryset = queryset.filter(price_byn__gte=car_price_from)
        elif car_price_to:
            queryset = queryset.filter(price_byn__lte=car_price_to)

    elif currency == 'USD':
        if car_price_from and car_price_to:
            queryset = queryset.filter(price_usd__range=(car_price_from, car_price_to))
        elif car_price_from:
            queryset = queryset.filter(price_usd__gte=car_price_from)
        elif car_price_to:
            queryset = queryset.filter(price_usd__lte=car_price_to)

    if car_engine_from and car_engine_to:
        car_engine_from = car_engine_from.split(' ')[0].replace(',', '.')
        car_engine_from = " " + car_engine_from
        car_engine_to = car_engine_to.split(' ')[0].replace(',', '.')
        car_engine_to = " " + car_engine_to
        queryset = queryset.filter(engine__range=(car_engine_from, car_engine_to))
    elif car_engine_from:
        car_engine_from = car_engine_from.split(' ')[0].replace(',', '.')
        car_engine_from = " " + car_engine_from
        queryset = queryset.filter(engine__gte=car_engine_from)
    elif car_engine_to:
        car_engine_to = car_engine_to.split(' ')[0].replace(',', '.')
        car_engine_to = " " + car_engine_to
        queryset = queryset.filter(engine__lte=car_engine_to)

    if car_transmission:
        car_transmission = car_transmission.lower()
        queryset = queryset.filter(transmission=car_transmission)

    if car_body:
        queryset = queryset.filter(car_body=car_body)

    if car_fuel:
        car_fuel = " " + car_fuel
        queryset = queryset.filter(fuel=car_fuel)

    if car_drive:
        queryset = queryset.filter(car_drive=car_drive)

    paginator = PaginationFilteredCars()
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    serializer = CarSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)
