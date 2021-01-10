# -*- coding: utf-8 -*-

import locale, datetime

locale.setlocale(locale.LC_ALL, '')

hoy = datetime.date.today()

formato = "%c"

hoy_formateado = hoy.strftime(formato)

print hoy
print hoy_formateado

