import datetime

from django.views.generic import TemplateView

import calendar


class CalendarView1(TemplateView):
    template_name = 'mycalendar/index.html'


class CalendarView2(TemplateView):
    template_name = 'mycalendar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        now = datetime.date.today()
        week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        days = calendar.monthcalendar(year, month)
        next_month = get_next_month(year, month)
        previous_month = get_prevous_month(year, month)

        context['cal'] = {
            'now': now,
            'week': week,
            'days': days,
        }
        return context
