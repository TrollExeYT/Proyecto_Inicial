from django.urls import path, include
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('sign_up', user_signup, name='sign_up'),
]