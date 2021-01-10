# -*- coding: utf-8 -*-

import locale, datetime, calendar

def validarFecha(fec):
	valido = False
	try:
		datetime.datetime.strptime(fec, '%d/%m/%Y')
		valido = True
	except ValueError:
		print "Formato de fecha incorrecta; debería ser día/mes/año"
	finally:
		return valido

# Programa principal 
locale.setlocale(locale.LC_ALL, "es_ES.UTF-8")
calendar.LocaleTextCalendar(calendar.SUNDAY)
calendario2 = calendar.HTMLCalendar(calendar.SUNDAY)
fechaString = raw_input("Por favor introduzca una fecha en formato DD/MM/YYYY: ")
if validarFecha(fechaString):
	# extraer dia
	fechaDate = datetime.datetime.strptime(fechaString, '%d/%m/%Y')  # -> de fecha a hora
	# Imprime el mes de esa fecha
	print "=" * 20
	cadenaCalendario = calendar.month(fechaDate.year,fechaDate.month)
	print cadenaCalendario #-> ¿por qué no imprime los acentos de sá - sábado -?
	print "=" * 20
	# Imprime en formato HTML
	cadenaHTML = str(calendario2.formatmonth(fechaDate.year,fechaDate.month))
	cadenaHTML = cadenaHTML.replace('>'+str(fechaDate.day)+'<','><span style="color:red;">'+str(fechaDate.day)+'</span><')
	print cadenaHTML

