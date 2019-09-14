from django.shortcuts import render
from django.db import models

from .models import User, Event

# Create your views here.
def catalog(request, category):
    events = Event.objects.filter(category=category)
    return render(request, 'catalog.html', {})
