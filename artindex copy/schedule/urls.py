from django.urls import path, include

from .views import CalendarView, event


##calendar

app_name = 'schedule'

urlpatterns = [
    path('schedule/calendar/', CalendarView.as_view(), name='calendar'),
    path('event/new/', event, name='event-new'),
    #path('schedule/event/edit/<int:event_id>', event, name='event_edit'),
]
