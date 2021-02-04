from django.http import HttpResponse
from django.shortcuts import render


def dashboard(request):
    return HttpResponse("Welcome to AllToys!")