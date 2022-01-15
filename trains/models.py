from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from cities.models import City


# Create your models here.


class Train(models.Model):
    train_name = models.CharField(max_length=50, unique=True, verbose_name='Название поезда')
    train_travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')  # in hours
    train_from_city = models.ForeignKey(City,
                                      on_delete=models.CASCADE,
                                      related_name='from_city_set',
                                      verbose_name='Поезд следует из')
    train_to_city = models.ForeignKey(City,
                                      on_delete=models.CASCADE,
                                      related_name='to_city_set',
                                      verbose_name='Поезд следует в')
    def __str__(self):
        return f'Поезд №{self.train_name} из города {self.train_from_city}'

    class Meta:
        verbose_name='Поезд'
        verbose_name_plural='Поезда'
        ordering=['train_name']

    def get_absolute_url(self):
        return reverse('trains:detail', kwargs={'pk': self.pk}) #check object name

    def clean(self):
        if self.train_from_city == self.train_to_city:
            raise ValidationError('Город прибытия не может быть городом отправления')
        qs=Train.objects.filter(train_to_city = self.train_to_city,
                                train_from_city = self.train_from_city,
                                train_travel_time= self.train_travel_time
                                ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Такой поезд уже имеется')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
