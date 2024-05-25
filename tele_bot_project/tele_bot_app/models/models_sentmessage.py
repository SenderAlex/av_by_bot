
from django.db import models
from django.urls import reverse
from django.utils import timezone

class SentMessage(models.Model):
    id = models.AutoField(primary_key=True)
    telegram_id = models.PositiveBigIntegerField(null=True, verbose_name="telegram_id")
    message = models.TextField(null=True, verbose_name="Сообщения")
    sentmessage_time = models.DateTimeField(default=timezone.now, verbose_name="Дата и время отправления")
    is_sent = models.BooleanField(default=False, verbose_name="Отметка об отправлении")



    def __str__(self):
        return f'{self.telegram_id}, {self.message}, {self.sentmessage_time}'

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})


    class Meta:
        verbose_name = 'Отправленное сообщение'
        verbose_name_plural = 'Отправленные сообщения'
        ordering = ('sentmessage_time',)


    def clean(self):  # чтобы id  был NOT NULL!!!
        if not self.id:
            self.id = SentMessage.objects.last().id + 1
