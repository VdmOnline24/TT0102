from django.contrib import admin
from routes.models import Route
# Register your models here.


class RouteAdmin(admin.ModelAdmin):

    class Meta():
        model=Route

    list_display = [
        'route_name',
        'route_to_city',
        'route_from_city',
        'route_travel_time',

        ]
    #list_editable = ['train_travel_time',]

admin.site.register(Route, RouteAdmin)