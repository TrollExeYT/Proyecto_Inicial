from django.shortcuts import render
from .models import *


# Create your views here.
def test(request):
    return render(request, 'base.html')


def add_event(request):
    if request.method == "POST":
        data = request.POST
        if 0 < int(data["division"]) < 2 or 0 < int(data["subdivision"]) < 2:
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