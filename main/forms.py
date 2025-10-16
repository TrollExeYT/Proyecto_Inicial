from django import forms
from main.models import Calendar

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['name', 'photo']
        labels = {
            'name': 'Nombre',
            'photo': 'Foto',
        }