# *-* coding: utf-8 *-*

def fibo(n):
	m=n-1 # El elemento "10", el n, en realidad en la lista es el elemento "9", el m.
	if m<=1:
		return lista[m] # Si m es menor o igual que 1, retorna el elemento de la lista
	else:
		lista[m]=fibo(n-1)+fibo(n-2) # Si m>=2, el elemento de fibonacci se calcula con el anterior y el anterior del anterior
		return lista[m]

n=1
lista={0:0,1:1}
while n>=1 and n<=100:
	n = int(raw_input("Elemento \"N\" de la sucesión de Fibonacci: "))
	if n>0:
		print ("El elemento en el lugar %d de la sucesión de Fibonacci es el %d") % (n,fibo(n))
		print lista
