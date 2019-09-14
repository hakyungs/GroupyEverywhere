from django.shortcuts import render

from .models import Event
from .forms import CatalogForm

# Create your views here.
def catalog(request, category):
    events = Event.objects.filter(category=category)

    if request.method == 'POST':
        form = CatalogForm()
    else:
        form = CatalogForm()

    context = {
        'form': form,
        'events': events,
    }

    return render(request, 'catalog.html', context)
