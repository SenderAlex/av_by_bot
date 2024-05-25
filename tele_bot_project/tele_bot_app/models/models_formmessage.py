
from django.db import models
from django.urls import reverse
from django.utils import timezone


class FormMessage(models.Model):
    form_message = models.TextField(null=True, verbose_name="Форма для отправки сообщения")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания сообщения")
    is_done = models.BooleanField(default=False, verbose_name="Отметка об отправлении")

    def __str__(self):
        return f'{self.form_message}, {self.created_time}'

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

