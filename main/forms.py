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
    """pass
    class Meta:
        model = EventConnector
        fields = ['day', 'group', 'division', 'event']
        widgets = {
            'day': forms.DateInput(attrs={'type': 'number', 'max': len(EventConnector.DAYS), 'min': 0}),
            'group': forms.DateInput(attrs={'type': 'number', 'max': len(EventConnector.GROUPS), 'min': 0}),
            'division': forms.DateInput(attrs={'type': 'number', 'max': len(EventConnector.DIVISIONS), 'min': 0}),
            'event': forms.DateInput(attrs={'type': 'number', 'max': len(EventConnector.objects.all()), 'min': 0}),
        }"""
