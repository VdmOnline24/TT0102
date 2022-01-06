from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from cities.forms import *
from cities.models import City
# Create your views here.
__all__=[
    'homepagefunc',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView',
    'CityListView',
]
# Homepage func
# Получает из бд список городов
def homepagefunc(request, pk=None):
#    if pk:
#        city=City.objects.filter(id=pk).first()
#        context={'object':city}
#        return render(request, 'cities/detail.html', context)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    qs=City.objects.all()
    form = CityForm()

    lst = Paginator(qs, 3)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)

    #context = {'object_list':qs, 'form':form}
    context = {'page_obj':page_obj, 'form':form}

    return render(request,'cities/homepage.html',context)

#Через ООП

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:homepage')

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:homepage')

class CityDeleteView(DeleteView):
    model = City
#    form_class = CityForm
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:homepage')

class CityListView(ListView):
    paginate_by = 3
    model = City
    template_name = 'cities/homepage.html'