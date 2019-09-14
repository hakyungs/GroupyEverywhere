from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CreateEventForm
from catalog.models import Event, User

# Create your views here.
def create(request):
    if request == "POST":
        form = CreateEventForm(request.POST)
        if form.is_valid():
            cur_user = User(
                name="",
                andrewID=request.user,
            )
            cur_user.save()
            new_event = Event(
                title=form.title, 
                description=form.description, 
                category=form.category, 
                startTime=form.clean_startTime(), 
                endTime=form.clean_endTime(),
                capacity=form.capacity,
                size=0,
                leader=cur_user
            )
            new_event.save()
        return
    else:
        form = CreateEventForm()
    return render(request, "create.html", {'form': form})