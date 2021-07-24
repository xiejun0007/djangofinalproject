from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')

def aboutpeoples(request):
    return render(request, 'pages/aboutpeoples.html')

def aboutpets(request):
    return render(request, 'pages/aboutpets.html')

