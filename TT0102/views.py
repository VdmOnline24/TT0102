from django.http import HttpResponse
from django.shortcuts import render



params={'Param1':'ParametrOne',
        'Param2':'ParametrTwo'}


def home(request):
    return render(request,'homepage.html',params)
