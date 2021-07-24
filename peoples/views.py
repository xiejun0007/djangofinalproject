from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Person

def index(request):

    peoples = Person.objects.all()
    paginator = Paginator(peoples, 6)
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
