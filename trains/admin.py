from django.contrib import admin
from trains.models import Train
# Register your models here.


class TrainAdmin(admin.ModelAdmin):

    class Meta():
        model=Train

    list_display = [
        'train_name',
        'train_to_city',
        'train_from_city',
        'train_travel_time',
        ]
    list_editable = ['train_travel_time',]

admin.site.register(Train, TrainAdmin)