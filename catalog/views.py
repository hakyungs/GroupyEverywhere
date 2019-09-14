from django.shortcuts import render
from django.views import generic

from .models import Event
from .forms import CatalogForm

# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    queryset = Event.objects.filter(category="FOOD").order_by("-endTime")
    template_name = 'catalog.html'


class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event.html'
