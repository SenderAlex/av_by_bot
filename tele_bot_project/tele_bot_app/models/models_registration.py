
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Registration(models.Model):
    #id = models.AutoField(primary_key=True)  ##
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return (f'{self.username}, {self.email}, {self.password}')

    # def get_absolute_url(self):
    #     return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Регистрация пользователей'
        verbose_name_plural = 'Регистрация пользователей'
        ordering = ['id']
