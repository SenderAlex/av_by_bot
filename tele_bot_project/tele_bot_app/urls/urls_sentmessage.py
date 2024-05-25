
from django.urls import path, include
from rest_framework import routers
from ..views.views_sentmessage import SentMessageViewSet
from ..views.views_message_for_telegram import create_sent_message


router12 = routers.DefaultRouter()
router12.register('sentmessage', SentMessageViewSet)


urlpatterns = [
    path('', include(router12.urls)),
    path('create-sent-message/<int:telegram_id>/<str:message>/', create_sent_message, name='create-sent-message'),
]
