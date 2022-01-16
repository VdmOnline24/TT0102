from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City
from trains.models import Train


# Create your models here.


class Route(models.Model):
    route_name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    route_travel_time = models.PositiveSmallIntegerField(verbose_name='Время маршрута')  # in hours
    route_from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='route_from_city_set',
        verbose_name='Начальный пункт')
    route_to_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='route_to_city_set',
        verbose_name='Конечный путь')
    route_trains = models.ManyToManyField(
        Train,
        verbose_name='Список поездов' )
    def __str__(self):
        return f'Маршрут №{self.route_name} из города {self.route_from_city} в город {self.route_to_city}'

    class Meta:
        verbose_name='Маршрут'
        verbose_name_plural='Маршруты'
        ordering=['route_name']

    def get_absolute_url(self):
        return reverse('routes:route_detail', kwargs={'pk': self.pk}) #check object name

    def clean(self):
        if self.route_to_city == self.route_from_city:
            raise ValidationError('Город прибытия не может быть городом отправления')

        qs= Route.objects.filter( route_to_city= self.route_to_city,
            route_from_city = self.route_from_city,
            route_travel_time= self.route_travel_time
            ).exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError('Такой маршрут уже имеется')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
