from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CalendarForm, AddEventForm
from .models import *


def user_login(request):
    if request.user.is_authenticated:
        return redirect('select_calendar')

    context = {
        'form': AuthenticationForm(),
        'message': '',
    }
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context['message'] = 'Usuario y/o Contraseña incorrecta.'
            return render(request, 'testing/login.html', context)
        login(request, user)
        return redirect('select_calendar')
    return render(request, 'testing/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    if request.user.is_authenticated:
        return redirect('select_calendar')

    context = {
        'form': UserCreationForm(),
        'message': '',
    }

    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2'] and UserCreationForm(request).is_valid():
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                context['message'] = 'Usuario creado correctamente'
            except ValueError:
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
def create_calendar(request):
    if request.method == "POST":
        try:
            calendar = Calendar.objects.create(user=request.user, name=request.POST['name'],
                                               photo=request.POST['photo'])
            calendar.save()
            return redirect('view_calendar', calendar_id=calendar.id)
        except ValueError:
            pass

    return render(request, 'testing/create_calendar.html', {'form': CalendarForm()})
@login_required(login_url='login')
def delete_calendar(request, calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    if calendar.user != request.user:
        return redirect('select_calendar')
    calendar.delete()
    return redirect('select_calendar')

@login_required(login_url='login')
def view_calendar(request, calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    if calendar.user != request.user:
        return redirect('select_calendar')

    context = {
        'info': calendar,
        'events_calendar': EventConnector.objects.filter(calendar=calendar).order_by(
            'day',
            'group',
            'division',
        ),
    }

    return render(request, 'testing/calendar.html', context)

@login_required(login_url='login')
def edit_calendar(request, calendar_id):
    calendar = Calendar.objects.get(id=calendar_id)
    if calendar.user != request.user:
        return redirect('select_calendar')

    context = {
        'form': AddEventForm,
        'info': calendar,
        'events': Event.objects.all().order_by('name'),
        'con_confirmed': EventConnector.objects.filter(calendar=calendar, confirmed=True),
        'con_unconfirmed': EventConnector.objects.filter(calendar=calendar, confirmed=False),
    }
    return render(request, 'testing/calendar_edit.html', context)

@login_required(login_url='login')
def confirm_events(request, calendar_id):
    if Calendar.objects.get(id=calendar_id).user != request.user:
        return redirect('select_calendar')

    data = EventConnector.objects.filter(
        calendar_id=calendar_id,
        confirmed=False,
    )

    for event in data:
        pre_event = EventConnector.objects.filter(
            calendar_id=calendar_id,
            day=event.day,
            group=event.group,
            division=event.division,
            confirmed=True,
        )

        if pre_event.exists():
            pre_event.delete()

        event.confirmed = True

    return redirect('view_calendar', calendar_id=calendar_id)

@login_required(login_url='login')
def undo_events(request, calendar_id):
    if Calendar.objects.get(id=calendar_id).user != request.user:
        return redirect('select_calendar')

    data = EventConnector.objects.filter(
        calendar_id=calendar_id,
        confirmed=False,
    )

    for event in data:

        event.delete()

    return redirect('edit_calendar', calendar_id=calendar_id)

@login_required(login_url='login')
# Es solo una idea y si encontramos una manera mas optimizada usaremos esa - B
def add_event(request, calendar_id):
    if Calendar.objects.get(id=calendar_id).user != request.user:
        return redirect('select_calendar')

    try:
        pre_event = EventConnector.objects.filter(
            calendar_id=calendar_id,
            day=request.POST['day'],
            group=request.POST['group'],
            division=request.POST['division'],
            confirmed=False,
        )

        if pre_event.exists():
            pre_event.delete()

        connector = EventConnector.objects.create(
            day=request.POST['day'],
            group=request.POST['group'],
            division=request.POST['division'],
            calendar=Calendar.objects.get(id=calendar_id),
            event_id=request.POST['event'],
            confirmed=False
        )
        connector.save()
    except ValueError:
        pass

    return redirect('edit_calendar', calendar_id=calendar_id)