from ..models.models_car_year import Car_Year
from rest_framework import serializers


class Car_YearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Year
        fields = ('id', 'car_year')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}