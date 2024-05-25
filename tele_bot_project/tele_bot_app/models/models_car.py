
from django.db import models
from django.urls import reverse


class Car(models.Model):
    id = models.AutoField(primary_key=True)
    car_title = models.CharField(max_length=255, verbose_name="Название авто", null=True)
    car_model = models.CharField(max_length=255, verbose_name="Модель авто", null=True)
    car_generation = models.CharField(max_length=255, verbose_name="Поколение авто", null=True)
    car_vin = models.CharField(max_length=255, verbose_name="VIN авто", null=True)
    main_car_image = models.URLField(verbose_name="Главная фото", null=True)
    car_images = models.URLField(verbose_name="Фотографии", null=True)
    year = models.IntegerField(null=True, verbose_name="Год выпуска")
    transmission = models.CharField(max_length=255, verbose_name="Трансмиссия", null=True)
    engine = models.CharField(max_length=255, verbose_name="Объём в литрах", null=True)
    fuel = models.CharField(max_length=255, verbose_name="Тип двигателя", null=True)
    car_body = models.CharField(max_length=255, verbose_name="Тип кузова", null=True)
    car_drive = models.CharField(max_length=255, verbose_name="Привод", null=True)
    car_color = models.CharField(max_length=255, verbose_name="Цвет авто", null=True)
    horse_power = models.CharField(max_length=255, verbose_name="л.с.", null=True)
    consumption = models.CharField(max_length=255, verbose_name="Расход", null=True)
    mileage = models.IntegerField(null=True, verbose_name="Пробег автомобиля")
    price_byn = models.IntegerField(verbose_name='Цена в бел. рублях', null=True)
    price_usd = models.IntegerField(verbose_name='Цена в долларах', null=True)
    city = models.CharField(max_length=255, verbose_name="Город", null=True)
    description = models.TextField(null=True, verbose_name="Описание")
    car_options = models.TextField(null=True, verbose_name="Комплектация")
    http_link = models.URLField(null=True, verbose_name="Ссылка")


    def __str__(self):
        return (f'{self.car_title}, {self.car_model}, {self.car_generation} {self.car_vin}, {self.main_car_image}, '
                f'{self.car_images}, {self.year}, {self.transmission}, {self.engine}, {self.fuel}, {self.car_body}, '
                f'{self.car_drive}, {self.car_color}, {self.horse_power}, {self.consumption}, {self.mileage}, '
                f'{self.price_byn}, {self.price_usd}, {self.city}, {self.description}, {self.car_options}, '
                f'{self.http_link}')

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
        ordering = ['id']


    def clean(self):  # чтобы id  был NOT NULL!!!
        if not self.id:
            self.id = Car.objects.last().id + 1
