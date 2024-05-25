from ..models.models_messagedata import MessageData
from rest_framework import serializers



class MessageDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageData
        fields = ('id', 'telegram_id', 'first_name', 'last_name', 'phone_number', 'message', 'full_date_time')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}
