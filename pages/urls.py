from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutpeoples', views.aboutpeoples, name= 'aboutpeoples'),
    path('aboutpets', views.aboutpets, name= 'aboutpets')
]
