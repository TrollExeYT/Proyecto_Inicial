from django.shortcuts import render
from .models import *


def test(request):
    return render(request, 'base.html')


def add_event(request):
    if request.method == "POST":
        data = request.POST
        max_div = len(EventConnector.DIVISIONS)
        if 0 < int(data["division"]) < max_div or 0 < int(data["subdivision"]) < max_div:
            try:
                connection = EventConnector(
                    calendar_id=request.POST['calendar_id'],
                    event_id=request.POST['event_id'],
                    division_id=request.POST['division'],
                    subdivision_id=request.POST['subdivision'],
                )
                connection.save()
            except Exception as e:
                print(e)
        else:
            pass
    else:
        pass