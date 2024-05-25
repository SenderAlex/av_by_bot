from ..models.models_sentmessage import SentMessage
from rest_framework import serializers


class SentMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentMessage  # MessageData??????
        fields = ('id', 'telegram_id',  'message', 'sentmessage_time', 'is_sent')
        # можно вместо всех этих полей '__all__'
        extra_kwargs = {'id': {'read_only': False}}