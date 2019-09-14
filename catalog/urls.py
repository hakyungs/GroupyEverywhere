from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.EventListView.as_view(), name='catalog'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
]