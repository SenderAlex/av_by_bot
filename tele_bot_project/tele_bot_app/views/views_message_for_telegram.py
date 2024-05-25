
from ..models.models_post import Post
from ..models.models_sentmessage import SentMessage
from ..models.models_formmessage import FormMessage

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .telegram_utils import send_telegram_message, send_select_user_telegram_message, send_form_telegram_message
from django.urls import reverse



def send_post_to_telegram_view(request):
    post = Post.objects.first()
    send_telegram_message(post=post)
    return HttpResponse("Send telegram message")


def send_message_to_telegram_view(request):
    sentmessage = SentMessage.objects.first()
    send_select_user_telegram_message(sentmessage=sentmessage)
    return HttpResponse("Send telegram answer")

def send_formmessage_to_telegram_view(request):
    formmessage = FormMessage.objects.first()
    send_form_telegram_message(formmessage=formmessage)
    return HttpResponse("Send telegram answer")


def create_sent_message(request, telegram_id, message):
    # создание объекта класса SentMessage
    sent_message = SentMessage.objects.create(telegram_id=telegram_id, message=message)
    # перенаправление на страницу где вводятся данные модели SentMessage
    url = reverse('admin:tele_bot_app_sentmessage_change', args=[sent_message.id])
    return HttpResponseRedirect(url)


