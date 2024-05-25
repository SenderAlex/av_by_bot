from ..models.models_car_transmission import Car_Transmission
from rest_framework import serializers



class Car_TransmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car_Transmission
        fields = ('id', 'car_transmission')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}