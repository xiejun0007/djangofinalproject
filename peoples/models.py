from django.db import models
from datetime import date, datetime

from django.db.models.fields import BLANK_CHOICE_DASH


class Person(models.Model):
    name = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField()
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
