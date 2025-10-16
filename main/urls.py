from django.urls import path
from .views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', user_signup, name='signup'),
    path('select_calendar/', select_calendar, name='select_calendar'),
    path('create_calendar/', create_calendar, name='create_calendar'),
    path('delete_calendar/<int:calendar_id>/', delete_calendar, name='delete_calendar'),
    path('calendar/<int:calendar_id>/', view_calendar, name='calendar'),
    path('edit_calendar/<int:calendar_id>/', edit_calendar, name='edit_calendar'),
    # RECORDATORIO QUE ESTO ES UNA IDEA  - B
    path('edit_calendar/<int:calendar_id>/add_event_<int:event_id>/day_<int:day>/group_<int:group>/division_<int:division>/', add_event, name='add_event'),
]