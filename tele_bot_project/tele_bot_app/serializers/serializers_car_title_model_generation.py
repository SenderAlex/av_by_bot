from ..models.models_car_title_model_generation import (Car_Title, Car_Model, Car_Generation)
from rest_framework import serializers


class Car_TitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Title
        fields = ('id', 'car_title')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}

#################

class Car_ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Model
        fields = ('id', 'car_model', 'car_title_id')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}

#################

class Car_GenerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Generation
        fields = ('id', 'car_generation', 'car_model_id')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}

