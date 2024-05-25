from ..models.models_car import Car
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'car_title', 'car_model', 'car_generation', 'car_vin', 'main_car_image', 'car_images',
                  'year', 'transmission', 'engine', 'fuel', 'car_body', 'car_drive', 'car_color', 'horse_power',
                  'consumption', 'mileage', 'price_byn', 'price_usd', 'city', 'description', 'car_options',
                  'http_link')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': True}}
