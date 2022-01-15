from django.urls import path

from trains.views import *


urlpatterns = [
    path('trains/', TrainListView.as_view(), name='trains_page'),
    path('trains/detail/<int:pk>/', TrainDetailView.as_view(), name='train_detail'),
    path('trains/<int:pk>/update/', TrainUpdateView.as_view(), name='train_update'),
    path('trains/<int:pk>/delete', TrainDeleteView.as_view(), name='train_delete'),
    path('trains/create/', TrainCreateView.as_view(), name='train_create'),
]
#<int:equipment_pk>