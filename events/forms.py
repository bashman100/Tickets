from django import forms
from .models import Event


class AddEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('name', 'description', 'start_time', 'price', 'capacity', 'sold_out')
