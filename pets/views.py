from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def pets(request):
    return render(request, 'pets/pets.html')

def search(request):
    return render(request, 'pets/search.html')

def aboutpets(request):
    return render(request, 'pages/aboutpets.html')