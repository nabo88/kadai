from django.urls import path
from mycalendar.views import CalendarView1, CalendarView2

app_name = 'mycalendar'

urlpatterns = [
    path('', CalendarView1.as_view()),
    path('<int:year>/<int:month>', CalendarView2.as_view())
]