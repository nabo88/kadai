from datetime import date
import calendar

from django.views.generic import TemplateView


def get_next(year, month):
    if month == 12:
        return year+1, 1
    else:
        return year, month+1


def get_previous(year, month):
    if month == 1:
        return year-1, 12
    else:
        return year, month-1


class CalendarView(TemplateView):
    template_name = 'mycalendar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = ''

        if self.kwargs.get('year'):
            year = self.kwargs.get('year')
        else:
            year = date.today().year

        if self.kwargs.get('month'):
            month = self.kwargs.get('month')
        else:
            month = date.today().month

        if date.today() == date(year, month, date.today().day):
            today = date.today().day

        days = calendar.monthcalendar(year, month)
        next_year, next_month = get_next(year, month)
        previous_year, previous_month = get_previous(year, month)

        context['cal'] = {
            'now': "{}年{}月".format(year, month),
            'days': days,
            'today': today,
            'next_year': next_year,
            'next_month': next_month,
            'previous_year': previous_year,
            'previous_month': previous_month,
         }
        return context
