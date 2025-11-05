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

class AddEventConnectorForm(forms.ModelForm):
    class Meta:
        model = EventConnector
        fields = ['day', 'group', 'division', 'event']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'number', 'min': 0}),
            'group': forms.DateInput(attrs={'type': 'number', 'min': 0}),
            'division': forms.DateInput(attrs={'type': 'number', 'min': 0}),
            'event': forms.DateInput(attrs={'type': 'number', 'min': 0}),
        }
