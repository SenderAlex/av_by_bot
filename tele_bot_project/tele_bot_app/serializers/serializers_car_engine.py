from ..models.models_car_engine import Car_Engine
from rest_framework import serializers



class Car_EngineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Engine
        fields = ('id', 'car_engine')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}