# *-* coding: utf-8 *-*

lista = [0.0,1.0]

n = int(input("Elemento \"N\" de la sucesión de Fibonacci: "))

for i in range(0,n-2):
	lista.append(lista[i]+lista[i+1])

print (lista)


