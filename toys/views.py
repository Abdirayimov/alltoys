from django.shortcuts import render
from django.utils import timezone

from toys.models import Toy


def dashboard(request):
    return render(request, 'toys/dashboard.html', context={'welcome_text': 'welcome to alltoys'})


def get_toys(request):
    toys = Toy.objects.all()
    toys = toys.filter(created_at__isnull=True)
    toys = toys.select_related("user")
    toys = toys.prefetch_related("tags")
    return render(request, 'toys/toys.html', context={"toys": toys})
