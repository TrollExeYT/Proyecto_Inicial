from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    photo_path = models.TextField(blank=False, null=False)


class Calendar(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #photo = models.ImageField()

"""
class CalendarEvent(models.Model):
    RANGE = range(0,3)
    DIVISIONS = [
        (0, "Dia"),
        (1, "Tarde"),
        (2, "Noche"),
    ]
    division = models.IntegerField(choices=DIVISIONS, default=0)
    position = models.IntegerField(choices=RANGE, default=0)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
"""