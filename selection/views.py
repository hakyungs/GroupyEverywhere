from django.shortcuts import render

from .constants import Activity, College

# Create your views here.
def selection(request):
    return render(request, "selection.html", {})

def activity(request):
    # A = Activity()
    # category_list = A.list_all()
    return render(request, "activity.html", {})

def study(request):
    return render(request, "study.html", {})

def food(request):
    return render(request, "food.html", {})

    