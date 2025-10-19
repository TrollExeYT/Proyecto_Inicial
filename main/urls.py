from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),
    path('select_calendar/', select_calendar, name='select_calendar'),
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('delete_calendar/<int:calendar_id>/', delete_calendar, name='delete_calendar'),
    path('edit_calendar/<int:calendar_id>/clean', clean_calendar, name='clean_calendar'),
    path('view_calendar/<int:calendar_id>/', view_calendar, name='view_calendar'),
    path('edit_calendar/<int:calendar_id>/', edit_calendar, name='edit_calendar'),
    # RECORDATORIO QUE ESTO ES UNA IDEA  - B
    path('edit_calendar/<int:calendar_id>/add_event/', add_event, name='add_event'),
    path('edit_calendar/<int:calendar_id>/confirm_events', confirm_events, name='confirm_events'),
    path('edit_calendar/<int:calendar_id>/undo_events', undo_events, name='undo_events'),
]