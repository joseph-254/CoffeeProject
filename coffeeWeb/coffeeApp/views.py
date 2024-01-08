from django.shortcuts import render
from django.http import HttpResponse

from . models import coffeeModel 

# Create your views here.

def index(request):
    # return HttpResponse("<h1>Hello world</h1>")

    all_coffee = coffeeModel.objects.all()
    context = {
        'coffees': all_coffee
    }
    return render(request, 'index.html', context )

def login(request):

    return render(request, 'login.html')
