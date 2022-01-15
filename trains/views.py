from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from trains.forms import *
from trains.models import Train
# Create your views here.
__all__=[
    'homepagefunc',
    'TrainDetailView',
    'TrainCreateView',
    'TrainUpdateView',
    'TrainDeleteView',
    'TrainListView',
]
# Homepage func
# Получает из бд список городов
def homepagefunc(request, pk=None):
    #form = TrainForm()
    qs=Train.objects.all()
    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj':page_obj}#, 'form':form}
    return render(request,'trains/trains_page.html',context)

#Через ООП

class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/train_detail.html'

class TrainCreateView(CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_create.html'
    success_url = reverse_lazy('trains:trains_page')

class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'trains/train_update.html'
    success_url = reverse_lazy('trains:trains_page')
    success_message = "Поезд успешно отредактирован"

class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/train_delete.html'
    success_url = reverse_lazy('trains:trains_page')

class TrainListView(ListView):
    paginate_by = 8
    model = Train
    template_name = 'trains/trains_page.html'



