# *-* coding:utf-8 *-*

import sys

try:
	divisor = int(raw_input("Divisor (escribe cero): "))
	dividendo = int(raw_input("Dividendo: "))
	print dividendo/divisor

except ZeroDivisionError:
	print "Por favor, no sé dividir entre cero"
	
except:
	for i in range(3):
		print("Error inesperado:", sys.exc_info()[i])

