from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def user_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'testing/login.html', {'message': 'Usuario y/o Contraseña incorrecta'})
        login(request, user)
        return redirect('select_calendar')
    return render(request, 'testing/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    context = {
        'form': UserCreationForm(),
        'message': '',
    }
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                context['message'] = 'Usuario creado correctamente'
            except:
                context['message'] = 'Ya existe un usuario con este nombre'
        else:
            context['message'] = 'Las contraseñas no coinciden'
    return render(request, 'testing/sign_up.html', context)


@login_required(login_url='login')
def select_calendar(request):
    context = {
        'info': Calendar.objects.filter(user=request.user),
    }
    return render(request, 'testing/calendar_select.html', context)

@login_required(login_url='login')
def calendar(request, calendar_id):
    if Calendar.objects.get(id=calendar_id).user != request.user:
        return redirect('select_calendar')

    context = {
        'info': Calendar.objects.get(id=calendar_id),
        'events_calendar': EventConnector.objects.all().order_by(
            'day',
            'group',
            'division',
        ),
    }

    return render(request, 'testing/calendar.html', context)

@login_required(login_url='login')
def edit_calendar(request, calendar_id):
    context = {}
    return render(request, 'calendar_edit.html', context)

@login_required(login_url='login')
# Es solo una idea y si encontramos una manera mas optimizada usaremos esa - B
def add_event(request, calendar_id, event_id, day, group, division):
    context = {}
    if Calendar.objects.get(id=calendar_id).user != request.user:
        return redirect('select_calendar')

    try:
        event_connector = EventConnector.objects.create(day=day, group=group, division=division, event_id=event_id, calendar_id=calendar_id)
        event_connector.save()
    except :
        redirect(edit_calendar, calendar_id)
    return redirect('')