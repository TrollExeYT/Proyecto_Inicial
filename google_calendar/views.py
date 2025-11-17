from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from google_auth_oauthlib.flow import Flow
from .models import GoogleCredentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from main.models import Calendar, EventConnector 
from datetime import datetime, timedelta, time

SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def google_login(request):
    request.session['google_redirect_next'] = request.META.get('HTTP_REFERER', reverse('select_calendar'))
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
            }
        },
        scopes=SCOPES
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        prompt='consent',
        include_granted_scopes='true'
    )
    request.session['oauth_state'] = state
    return redirect(authorization_url)

@login_required
def google_callback(request):
    state = request.session.pop('oauth_state', None)
    flow = Flow.from_client_config(
        client_config={
            "web": {
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [settings.GOOGLE_REDIRECT_URI],
            }
        },
        scopes=SCOPES,
        state=state
    )
    flow.redirect_uri = settings.GOOGLE_REDIRECT_URI
    try:
        authorization_response = request.build_absolute_uri()
        flow.fetch_token(authorization_response=authorization_response)
        credentials = flow.credentials
        GoogleCredentials.objects.update_or_create(
            user=request.user,
            defaults={'credentials_json': credentials.to_json()}
        )
    except Exception as e:
        pass
    redirect_url = request.session.pop('google_redirect_next', reverse('select_calendar'))
    return redirect(redirect_url)

@login_required
def export_options_page(request, calendar_id):
    context = {
        'calendar_id': calendar_id
    }
    return render(request, 'google_calendar/export_options.html', context)

TIME_MAP = {
    (0, 0): time(8, 0),
    (0, 1): time(9, 0),
    (0, 2): time(10, 0),
    (1, 0): time(14, 0),
    (1, 1): time(15, 0),
    (1, 2): time(16, 0),
    (2, 0): time(19, 0),   
    (2, 1): time(20, 0),   
    (2, 2): time(21, 0),   
}
EVENT_DURATION = timedelta(hours=1)

@login_required
def export_calendar_events(request, calendar_id):

    num_weeks = 1 
    if request.method == "POST":
        try:
            num_weeks = int(request.POST.get('num_weeks', 1))
            if num_weeks < 1:
                num_weeks = 1
        except ValueError:
            num_weeks = 1

    try:
        creds_model = request.user.google_credentials
        credentials = creds_model.credentials
    except GoogleCredentials.DoesNotExist:
        return redirect('google_calendar:google_login')

    if credentials.expired and credentials.refresh_token:
        try:
            credentials.refresh(Request())
            creds_model.credentials = credentials
            creds_model.save()
        except Exception as e:
            return redirect('google_calendar:google_login')

    try:
        calendar = Calendar.objects.get(id=calendar_id, user=request.user)
        events_to_export = EventConnector.objects.filter(calendar=calendar, confirmed=True)
    except Calendar.DoesNotExist:
        return redirect('select_calendar')

    today = datetime.now().date()
    initial_start_of_week = today + timedelta(days=-today.weekday()) 
    if today.weekday() >= 0: 
        initial_start_of_week += timedelta(weeks=1)

    try:
        service = build('calendar', 'v3', credentials=credentials)

        for week_num in range(num_weeks):

            current_week_start_date = initial_start_of_week + timedelta(weeks=week_num)

            for event_con in events_to_export:
                event_name = event_con.event.name
                if event_name == 'Default':
                    continue

                event_day_offset = event_con.day
                event_start_time = TIME_MAP.get((event_con.group, event_con.division))

                if event_start_time is None:
                    continue 

                start_datetime = datetime.combine(
                    current_week_start_date + timedelta(days=event_day_offset),
                    event_start_time
                )
                end_datetime = start_datetime + EVENT_DURATION

                google_event = {
                    'summary': event_name,
                    'description': event_con.event.description, 
                    'start': {
                        'dateTime': start_datetime.isoformat(),
                        'timeZone': settings.TIME_ZONE, 
                    },
                    'end': {
                        'dateTime': end_datetime.isoformat(),
                        'timeZone': settings.TIME_ZONE, 
                    },
                }
                try:
                    service.events().insert(calendarId='primary', body=google_event).execute()
                except Exception as e:
                    pass
    except Exception as e:
        pass

    return redirect('view_calendar', calendar_id=calendar_id, type_view=0)