from ..models.models_car_engine_type import Car_EngineType
from rest_framework import serializers



class Car_EngineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_EngineType
        fields = ('id', 'car_engine_type')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}