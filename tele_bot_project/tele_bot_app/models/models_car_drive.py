
from django.db import models
from django.urls import reverse
from django.utils import timezone



class Car_Drive(models.Model):
    id = models.AutoField(primary_key=True)
    car_drive = models.CharField(max_length=255, verbose_name="Привод", null=True)

    def __str__(self):
        return (f'{self.car_drive}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Привод'
        verbose_name_plural = 'Приводы'
        ordering = ['id']
