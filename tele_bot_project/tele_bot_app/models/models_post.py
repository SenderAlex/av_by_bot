
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата и время отправления")
    is_published = models.BooleanField(default=False, verbose_name="Отметка об отправлении")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('created_at',)
