
from django.urls import path
from . import views
app_name = 'google_calendar'

urlpatterns = [
    path('login/', views.google_login, name='google_login'),
    path('callback/', views.google_callback, name='google_callback'),
    path('export/options/<int:calendar_id>/', views.export_options_page, name='export_options'),
    path('export/<int:calendar_id>/', views.export_calendar_events, name='export_calendar_events'),
]