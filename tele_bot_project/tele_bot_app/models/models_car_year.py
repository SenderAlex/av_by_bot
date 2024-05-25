
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Car_Year(models.Model):
    id = models.AutoField(primary_key=True)
    car_year = models.CharField(max_length=255, verbose_name="Год выпуска", null=True)

    def __str__(self):
        return (f'{self.car_year}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Год выпуска'
        verbose_name_plural = 'Годы выпуска'
        ordering = ['id']
