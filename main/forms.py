from django import forms
from main.models import Calendar, EventConnector


class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name', 'photo']
        labels = {
            'name': 'Nombre',
            'photo': 'Foto',
        }

class AddEventForm(forms.ModelForm):
    class Meta:
        model = EventConnector
        fields = "__all__"
