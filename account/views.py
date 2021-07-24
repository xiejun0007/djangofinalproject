# from contacts.models import Contact
# from django.db import models
from django.shortcuts import render
# from django.contrib import messages,auth
# from django.contrib.auth.models import User

def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')