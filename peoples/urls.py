from django.urls import path
from . import views

urlpatterns = [
    path('peoples', views.index, name='peoples'),
    path('<int:person_id>', views.person, name='person'),
    path('aboutpeoples', views.aboutpeoples, name='aboutpeoples'),
    # path('peoples', views.peoples, name='peoples')
]
