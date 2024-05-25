from ..models.models_registration import Registration
from rest_framework import serializers



class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registration
        fields = ('username', 'email', 'password')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': True}}
