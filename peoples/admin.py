from django.contrib import admin
from peoples.models import Person
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','list_date')

admin.site.register(Person, PersonAdmin)