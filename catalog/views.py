from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect

from .models import Event
from .forms import CreateForm, JoinForm

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
        event = Event(
            title=form.data["title"],
            description=form.data["content"],          
            category="FOOD",
            startTime=timezone.now(),
            endTime=timezone.now(),
            capacity=form.data["capacity"],       
            size=0,
            leader=form.data["andrewID"]
        )
        event.save()
        return HttpResponseRedirect('../')
    return render(request, 'create.html', {"form": form})

def join(request, pk):
    event = Event.objects.get(pk=pk)
    form = JoinForm()
    if request.method == "POST":
        form = JoinForm(request.POST)
        member = form.data["andrewID"]
        event.member += ", " + member
        event.size += 1
        event.save()
        return HttpResponseRedirect('../')
    return render(request, 'join.html', {"form": form})
        

class EventDetailView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event.html'
