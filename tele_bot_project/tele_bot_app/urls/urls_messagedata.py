
from django.urls import path, include
from rest_framework import routers
from ..views.views_messagedata import MessageDataViewSet
from ..views.views_message_for_telegram import (send_post_to_telegram_view, send_message_to_telegram_view,
                                                send_formmessage_to_telegram_view)


router11 = routers.DefaultRouter()
router11.register('messagedata', MessageDataViewSet)


urlpatterns = [
    path('', include(router11.urls)),
    path('send_telegram/', send_post_to_telegram_view),
    path('send_answer/', send_message_to_telegram_view),
    path('send_formmessage/', send_formmessage_to_telegram_view),
]
