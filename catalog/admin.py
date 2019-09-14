from django.contrib import admin

from catalog.models import User, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Event)