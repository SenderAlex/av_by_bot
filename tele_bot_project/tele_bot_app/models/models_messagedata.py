
from django.db import models
from django.urls import reverse
from django.utils import timezone



class MessageData(models.Model):
    id = models.AutoField(primary_key=True)
    telegram_id = models.PositiveBigIntegerField(null=True, verbose_name="telegram_id")
    first_name = models.CharField(null=True, max_length=255, verbose_name="Имя пользователя")
    last_name = models.CharField(null=True, max_length=255, verbose_name="Фамилия пользователя")
    phone_number = models.CharField(null=True, max_length=255, verbose_name="Номер телефона")
    message = models.TextField(null=True, verbose_name="Сообщения")
    full_date_time = models.DateTimeField(default=timezone.now, verbose_name="Дата и время получения")


    def __str__(self):
        return (f'{self.telegram_id}, {self.first_name}, {self.last_name}, {self.phone_number}, '
                f'{self.message}, {self.full_date_time}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})


    class Meta:
        verbose_name = 'Полученное сообщение'
        verbose_name_plural = 'Полученные сообщения'
        ordering = ('full_date_time',)


    def clean(self):  # чтобы id  был NOT NULL!!!
        if not self.id:
            self.id = MessageData.objects.last().id + 1

