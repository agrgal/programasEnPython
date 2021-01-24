# *-* coding: utf-8 *-*

def fibo(n):
	m=n-1
	if m<=1:
		return m
	elif m in lista:
		return lista[m] #memoizacion
	else:
		lista[m]=fibo(n-1)+fibo(n-2)
		return lista[m]
		# return fibo(n-1)+fibo(n-2)

n=1
lista ={0:0,1:1} #diccionario.
while n>=1 and n<=100:
	n = int(raw_input("Elemento \"N\" de la sucesión de Fibonacci: "))
	if n>0:
		print ("El elemento en el lugar %d de la sucesión de Fibonacci es el %d") % (n,fibo(n))
		# print ("La lista es: %s") % (lista)


