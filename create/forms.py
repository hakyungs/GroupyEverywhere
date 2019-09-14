from django import forms

from bootstrap3_datetime.widgets import DateTimePicker

class CreateForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    description = forms.CharField(label="Description")
    category = forms.CharField(max_length=10)
    startTime = forms.DateTimeField(widget=DateTimePicker(options={"format": 'YYYY-MM-DD HH:mm', "pickSeconds": False}))
    endTime = forms.DateTimeField(widget=DateTimePicker(options={"format": 'YYYY-MM-DD HH:mm', "pickSeconds": False}))
    capacity = forms.IntegerField()
    size = forms.IntegerField()
