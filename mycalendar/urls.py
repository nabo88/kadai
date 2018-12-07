from django.urls import path
from mycalendar.views import CalendarView

app_name = 'mycalendar'

urlpatterns = [
    path('', CalendarView.as_view()),
    path('<int:year>/<int:month>', CalendarView.as_view(), name='month')
]