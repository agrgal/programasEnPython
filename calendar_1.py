# -*- coding: utf-8 -*-

import locale, datetime, calendar

locale.setlocale(locale.LC_ALL, '')

calendar.setfirstweekday(calendar.SUNDAY)

c = calendar.TextCalendar(calendar.MONDAY)

c.prmonth(2015,11).encode("utf-8")

c = calendar.HTMLCalendar(calendar.SUNDAY)
print c.formatmonth(2007, 7)

