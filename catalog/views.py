from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from .models import Event
from .forms import CreateForm

# Create your views here.
def catalog(request):
    event_list = Event.objects.all().order_by("-endTime")
    if request == "POST":
        pass
    return render(request, 'catalog.html', {'event_list': event_list})

def create(request):
    form = CreateForm()
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            event = Event(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["content"],
                category="FOOD",
                startTime=timezone.now(),
                endTime=timezone.now(),
                capacity=form.cleaned_data["capacity"],
                size = 0,
                leader=form.cleaned_data["andrewID"] 
            )
            event.save()
    return render(request, 'create.html', {"form": form})

class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event.html'
