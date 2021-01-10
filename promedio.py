# -*- coding:utf-8 -*-

import pydoc

def funcion(x):
	""" Esta función retorna un número distinto """
	y = (x * 20 ) / 5
	return y

suma = 0.0
conteo = 0

for i in range(10):
	for j in range (10):
		suma += funcion ((i+1) * (j+1))
		conteo += 1
		print conteo, suma

print suma / conteo



