
from django.db import models
from django.urls import reverse
from django.utils import timezone



class Car_Engine(models.Model):
    id = models.AutoField(primary_key=True)
    car_engine = models.CharField(max_length=255, verbose_name="Объём двигателя", null=True)

    def __str__(self):
        return (f'{self.car_engine}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Объём двигателя'
        verbose_name_plural = 'Объёмы двигателей'
        ordering = ['id']
