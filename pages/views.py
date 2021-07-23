from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def home(request):
    return render(request, 'pages/home.html')

