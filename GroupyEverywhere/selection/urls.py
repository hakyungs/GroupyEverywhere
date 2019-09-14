from django.urls import path
from selection import views

urlpatterns = [
    path('', views.selection, name='selection'),
    path('activity/', views.activity, name='activity'),
    path('study/', views.study, name='study'),
    path('food/', views.food, name='food'),
]