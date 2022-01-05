from django.shortcuts import render
from django.views.generic import DetailView

from cities.models import City
# Create your views here.
__all__=(
    'homepagefunc', 'CityDetailView',
)
# Homepage func
# Получает из бд список городов
def homepagefunc(request, pk=None):
#    if pk:
#        city=City.objects.filter(id=pk).first()
#        context={'object':city}
#        return render(request, 'cities/detail.html', context)
    if request.method == 'POST':
        print(request.POST)
    qs=City.objects.all()
    context = {'object_list':qs}
    return render(request,'cities/homepage.html',context)

#Через ООП

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'


