from django.shortcuts import render

# Create your views here.
def selection(request):
    return render(request, "selection.html", {})

def activities(request):
    return render(request, "activities.html", {})

def study(request):
    return render(request, "study.html", {})

def food(request):
    return render(request, "food.html", {})

    