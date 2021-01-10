# *-* coding: utf-8 *-*

import random

# =============================================================
# ALGORITMO DE ORDENACION POR INSERCIÓN DIRECTA
# =============================================================

# Genero un vector con 100 elementos colocados en posiciones aleatorias
misNumeros = []
for i in range(1,51):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)

# print misNumeros

# ================================
# Ordenacion por insercion directa
# ================================

misNumerosID = misNumeros[:] #COPIO los valores del array
indice=1 # corresponde a la SEGUNDA posicion del array, la posición cero es la primera
pivote = 0 # corresponde al pivote, que puede ser el último elemento del array

print "ANTES: ",misNumerosID
# print "Longitud del elemento: ",str(len(misNumerosID))
# print "Rango negativo: ",str(range(len(misNumerosID),0,-1))

while indice<len(misNumerosID): # mientras indice sea menor que la longitud. Acabará en el índice 9, el último, ya
	# que la longitud es 10. O en n, y el índice es n-1
	# print indice
	for i in range(indice,0,-1): #desde la posición indice hasta 1, 0 es el límite inferior. 
		# print " - ",str(misNumerosID[i])
		if misNumerosID[i]>misNumerosID[i-1]: # si el anterior es MENOR (l oúnico que cambia) que el que estoy evaluando...
			pivote = misNumerosID[i] # Asigno este al pivote
			misNumerosID[i]=misNumerosID[i-1] # al de la posición i le pongo el de la posición i-1
			misNumerosID[i-1]=pivote # a la posición i-1 pongo el pivote
			pivote=0
			# print misNumerosID
	indice+=1 #importante. Aumento el pivote en 1
print " = = = "
print "DESPUÉS: ",misNumerosID
