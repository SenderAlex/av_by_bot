from ..models.models_car_body import Car_Body
from rest_framework import serializers


class Car_BodySerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Body
        fields = ('id', 'car_body')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}