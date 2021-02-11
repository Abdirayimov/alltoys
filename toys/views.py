from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from toys.models import Toy


# Oddiy view
# def dashboard(request):
#     return render(request, 'toys/dashboard.html', context={'welcome_text': 'welcome to alltoys'})

# base view
# class DashboardView(View):
#     def get(self, request):
#         return render(request, 'toys/dashboard.html', context={'welcome_text': 'welcome to alltoys'})

# Template view
class DashboardView(TemplateView):
    template_name = 'toys/dashboard.html'
    extra_context = {'welcome_text': 'welcome to alltoys!'}


def get_toys(request):
    toys = Toy.objects.defer('created_at')  # only('user_id', 'created_at', 'name')
    toys = toys.filter(created_at__year=timezone.now().year)
    toys = toys.select_related("user")
    return render(request, 'toys/toys.html', context={"toys": toys})


def get_toy_detail(request, **kwargs):
    try:
        toy = Toy.objects.get(pk=kwargs.get('id'))
    except Exception:
        return redirect
    return render(request, 'toys/toy_detail.html', context={'toy': toy})
