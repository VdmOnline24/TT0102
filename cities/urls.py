from django.urls import path

from cities.views import *


urlpatterns = [

    path('', homepagefunc, name='homepage'),
    #path('<int:pk>/', homepagefunc, name='homepage'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]
