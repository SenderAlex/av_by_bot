from ..models.models_car_drive import Car_Drive
from rest_framework import serializers



class Car_DriveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Drive
        fields = ('id', 'car_drive')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}
