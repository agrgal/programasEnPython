# -*- coding: utf-8 -*-

import datetime

hoy = datetime.date.today()

print hoy
print 'ctime:', hoy.ctime()
print 'tupla:', hoy.timetuple()
print 'ordinal:', hoy.toordinal()
print 'Año:', hoy.year
print 'Mes :', hoy.month
print 'Día :', hoy.day

print "Día mínimo: ", datetime.date.min
print "Día máximo: ", datetime.date.max
print "Resolución: ", datetime.date.resolution
