# *-* coding: utf-8 *-*

import random

def quicksort(L, principio, final):
	
	i = principio
	j = final
	# pivote = (L[i]+L[j])/2
	pivote=L[principio]
	
	while i<j:
		
		while L[i]>pivote: # SI ES DESCENDENTE CAMBIO EL SIGNO
			i=i+1
		
		while L[j]<pivote: # SI ES DESCENDENTE CAMBIO EL SIGNO
			j=j-1
			
		if i<=j:
			temporal = L[i]
			L[i]=L[j]
			L[j]=temporal
			# una vez los intercambio, aumento i y decremento j
			i = i + 1
			j = j - 1 

	# entra en juego la recursividad
	
	if i<final: # si la i es menor que final
		L = quicksort(L,i,final)
		
	if j>principio:
		L = quicksort(L,principio,j)
	
	# devolvemos la lista ordenada
	return L
    

# Genero un vector con 100 elementos colocados en posiciones aleatorias

misNumeros = []
for i in range(1,51):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)

# misNumeros = [8,4,7,5,3,2,1,6]

print "Mis números: ",misNumeros
print "= = = "
print quicksort(misNumeros,0,len(misNumeros)-1)
