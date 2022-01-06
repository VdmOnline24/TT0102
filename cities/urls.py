from django.urls import path

from cities.views import *


urlpatterns = [

    #path('', homepagefunc, name='homepage'),
    path('', CityListView.as_view(), name='homepage'),
    #path('<int:pk>/', homepagefunc, name='homepage'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('add/', CityCreateView.as_view(), name='create'),

]
