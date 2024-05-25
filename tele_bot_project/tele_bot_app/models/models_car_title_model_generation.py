
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Car_Title(models.Model):
    id = models.AutoField(primary_key=True)
    car_title = models.CharField(max_length=255, verbose_name="Наименование авто", null=True)


    def __str__(self):
        return (f'{self.car_title}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})


    class Meta:
        verbose_name = 'Название автомобиля'
        verbose_name_plural = 'Название автомобилей'
        ordering = ['id']

#####################

class Car_Model(models.Model):
    id = models.AutoField(primary_key=True)
    car_model = models.CharField(max_length=255, verbose_name="Наименование модели", null=True)
    car_title_id = models.ForeignKey(Car_Title, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.car_model}, {self.car_title_id}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Название модели'
        verbose_name_plural = 'Название моделей'
        ordering = ['id']

#####################

class Car_Generation(models.Model):
    id = models.AutoField(primary_key=True)
    car_generation = models.CharField(max_length=255, verbose_name="Наименование поколения", null=True)
    car_model_id = models.ForeignKey(Car_Model, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.car_generation}, {self.car_model_id}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Название поколения'
        verbose_name_plural = 'Название поколеней'
        ordering = ['id']

