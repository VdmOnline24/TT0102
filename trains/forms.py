from django import forms

from cities.models import City
from trains.models import Train

__all__ = [
    'TrainForm',
]

class TrainForm(forms.ModelForm):
    train_name = forms.CharField(
        label='Номер поезда',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер поезда'
        })
    )
    train_from_city = forms.ModelChoiceField(
        label='Станция отправления',
        queryset=City.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Выберите станцию отправления'
        })
    )
    train_to_city = forms.ModelChoiceField(
        label='Станция назначения',
        queryset=City.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Выберите станцию назначения'
        })
    )
    train_travel_time = forms.IntegerField(
        label='Номер поезда',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите время в пути'
        })
    )

    class Meta:
        model=Train
        fields='__all__'
