from django.shortcuts import render
from .forms import CreateForm

# Create your views here.
def create(request):
    if request == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            return 
    else:
        form = CreateForm()

    return render(request, "create.html", {'form': form})