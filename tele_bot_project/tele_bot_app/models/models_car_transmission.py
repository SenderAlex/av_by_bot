
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Car_Transmission(models.Model):
    id = models.AutoField(primary_key=True)
    car_transmission = models.CharField(max_length=255, verbose_name="Тип коробки передач", null=True)

    def __str__(self):
        return (f'{self.car_transmission}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Тип коробки передач'
        verbose_name_plural = 'Типы коробки передач'
        ordering = ['id']
