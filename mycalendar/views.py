from django.views import generic

from calendar import Calendar
from datetime import date


class CalendarView(generic.TemplateView):
    template_name = 'mycalendar/index.html'

    def get_month_data(self):
        data = {
            'year': self.kwargs.get('year'),
            'month': self.kwargs.get('month'),
            'week': ['Mon', 'Tue', "Wed", "Thu", "Fri", "Sat", "Sun"]
        }
        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month_data'] = self.get_month_data()
        return context