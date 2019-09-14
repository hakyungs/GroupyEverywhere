from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

class CreateEventForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description")
    category = forms.CharField(max_length=10)
    startTime = forms.DateTimeField()
    endTime = forms.DateTimeField()
    capacity = forms.IntegerField()

    def clean_startTime(self):
        data = self.cleaned_data['startTime']
        
        # Check if a date is not in the past. 
        if data < timezone.now():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Remember to always return the cleaned data.
        return data
