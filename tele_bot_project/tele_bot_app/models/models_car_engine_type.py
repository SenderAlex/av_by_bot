
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Car_EngineType(models.Model):
    id = models.AutoField(primary_key=True)
    car_engine_type = models.CharField(max_length=255, verbose_name="Тип двигателя", null=True)

    def __str__(self):
        return (f'{self.car_engine_type}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Тип двигателя'
        verbose_name_plural = 'Типы двигателей'
        ordering = ['id']


