# *-* coding: utf-8
from datetime import datetime, date, time, timedelta
import calendar

formato_fecha = "%d-%m-%Y"
hoy = datetime.strptime("01-01-2015", formato_fecha)
ayer = hoy-timedelta(days=1)  # Resta a la fecha actual 1 día
mannana = hoy + timedelta(days=1)  # Suma a la fecha actual 1 día
diferencia_en_dias = mannana-hoy  # Resta las dos fechas

hoy_mas_1_millon_segundos = hoy + timedelta(seconds=250e6)
ahora = datetime.now() 
hora_actual = time(ahora.hour, ahora.minute, ahora.second)
mas_5m = ahora + timedelta(seconds=300)
mas_5m = time(mas_5m.hour, mas_5m.minute, mas_5m.second)
racion_de_5h = timedelta(hours=5)
mas_5h = ahora + racion_de_5h
 
print("Ayer:", ayer)
print("Hoy:", hoy)
print("Mañana:", mannana)
print("Diferencia en días entre mañana y hoy:", diferencia_en_dias.days)
print("La fecha de hoy más 1 millón de segundos:", hoy_mas_1_millon_segundos)
print("Hora actual:", hora_actual)
print("Hora actual + 5 minutos:", mas_5m)
print("Hora actual + 5 horas:", mas_5h)
