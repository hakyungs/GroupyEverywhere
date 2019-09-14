from django.shortcuts import render
from django.db import models


# Create your views here.
def catalog(request):
    # events = Event.objects.filter(category=category)
    return render(request, 'catalog.html', {})
