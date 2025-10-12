from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *


def user_login(request):
    if request.method == "POST":
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'message': 'Usuario y/o Contraseña incorrecta'})
        login(request, user)
        return redirect('')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_signup(request):
    context = {}
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                user.save()
                context['message'] = 'Usuario creado correctamente'
            except:
                context['message'] = 'Ya existe un usuario con este nombre'
        else:
            context['message'] = 'Las contraseñas no coinciden'
    return render(request, 'sign_up.html', context)