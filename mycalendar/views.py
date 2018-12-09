from django.views.generic import TemplateView


import calendar


def get_next(year,month):
    if month == 12:
        return year+1, 1
    else:
        return year, month+1


def get_previous(year, month):
    if month == 1:
        return year-1, 12
    else:
        return year, month-1


class CalendarView1(TemplateView):
    template_name = 'mycalendar/index.html'


class CalendarView2(TemplateView):
    template_name = 'mycalendar/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        days = calendar.monthcalendar(year, month)
        next_year, next_month = get_next(year, month)
        previous_year, previous_month = get_previous(year, month)

        context['cal'] = {
            'now': "{}年{}月".format(year, month),
            'week': week,
            'days': days,
            'next_year': next_year,
            'next_month': next_month,
            'previous_year': previous_year,
            'previous_month': previous_month,
        }
        return context
