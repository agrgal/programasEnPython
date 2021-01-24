# *-* coding: utf-8 *-*

def factorial(n):
	if n<=1:
		return 1
	else:
		return factorial(n-1)*n

n=1
while n>=1 and n<=100:
	n = int(raw_input("Elemento \"N\" para calcularle el factorial: "))
	if n>0:
		print ("El factorial del número %d es %d") % (n,factorial(n))

