from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('<int:pk>', views.EventDetailView.as_view(), name='event_detail'),
]