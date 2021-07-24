import peoples
from django.db.models import query
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Person

def index(request):

    peoples = Person.objects.all()
    paginator = Paginator(peoples, 3)
    page = request.GET.get('page')
    paged_peoples = paginator.get_page(page)

    context= {
        'peoples' : paged_peoples
    }

    return render(request, 'peoples/peoples.html', context)

def person(request, person_id):

    person = get_object_or_404(Person, pk=person_id)

    context = {
        'person': person
    }

    return render(request, 'peoples/person.html', context)

def aboutpeoples(request):
    return render(request, 'pages/aboutpeoples.html')

def searchperson(request):
    
    queryset_list = Person.objects.all()
        
    #name
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
              name=keywords)        
            
   
                                
    context = {
        'values':request.GET,
        'peoples': queryset_list
    
    }
            
    return render(request,'peoples/searchperson.html', context)
            
