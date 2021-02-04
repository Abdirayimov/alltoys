from django.shortcuts import render
from .models import *


def dashboard(request):
    users = User.objects.all()
    toys = Toy.objects.all()
    context = {
        'users': users,
        'toys': toys
    }
    return render(request, 'toys/dashboard.html', context)
