# *-* coding: utf-8 *-*

cadena = ""
n = int(raw_input("Elemento a convertir en binario (1 al 1000): "))

while n>=2:
	cadena= str(n%2) + cadena
	n = n/2

cadena=str(n) + cadena

print cadena

