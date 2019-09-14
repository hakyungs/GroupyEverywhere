from django import forms

class CreateForm(forms.Form):
    andrewID = forms.CharField(max_length=20)
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=200)
    startTime = forms.DateTimeField()
    endTime = forms.DateTimeField()
    capacity = forms.IntegerField()
