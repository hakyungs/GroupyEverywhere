from django.shortcuts import render
from .forms import EventForm

# Create your views here.
def create(request):
    if request == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            return 
    else:
        form = EventForm()

    return render(request, "create.html", {'form': form})