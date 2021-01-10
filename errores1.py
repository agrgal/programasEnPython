# *-* coding:utf-8 *-*

try:
	divisor = int(raw_input("Divisor (escribe cero): "))
	dividendo = int(raw_input("Dividendo: "))
	print dividendo/divisor

except ZeroDivisionError:
	print "Por favor, no sé dividir entre cero"
	
except Exception, ex:
	print "Se ha producido otro tipo de error: " + str(ex)
