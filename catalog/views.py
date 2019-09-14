from django.shortcuts import render
from django.views import generic

from .models import Event
from .forms import CatalogForm

# Create your views here.
def catalog(request):
    event_list = Event.objects.filter(category="FOOD").order_by("-endTime")
    if request == "POST":
        pass
    return render(request, 'catalog.html', {'event_list': event_list})


class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event.html'
