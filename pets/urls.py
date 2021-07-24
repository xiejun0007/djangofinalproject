from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pets'),
    path('pets', views.pets, name='pets'),
    path('search', views.search, name='search'),
    path('aboutpets', views.aboutpets, name='aboutpets'),
    #path('<int:peoples_id>', views.person, name='person')
]
