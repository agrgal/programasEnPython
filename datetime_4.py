# -*- coding: utf-8 -*-

import datetime

hoy = datetime.date.today()

ahora = datetime.time(15,42,30)

print hoy, ahora

# combinando fecha y hora
combinadas = datetime.datetime.combine(hoy, ahora)
print combinadas

#  obteniendo formato fecha/hora desde ordinal y timestamp.
print datetime.datetime.fromordinal(384344)
print datetime.datetime.fromtimestamp(1232321321)

