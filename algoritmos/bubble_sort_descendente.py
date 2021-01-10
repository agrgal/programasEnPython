# *-* coding: utf-8 *-*

import random

# =============================================================
# ALGORITMO DE ORDENACION POR INSERCIÓN DIRECTA
# =============================================================

# Genero un vector con 100 elementos colocados en posiciones aleatorias
misNumeros = []
for i in range(1,31):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)

# print misNumeros

# ================================
# Ordenacion por insercion directa
# ================================

misNumerosID = misNumeros[:] #COPIO los valores del array
indice=len(misNumerosID)-1 # corresponde a la última posición del array
pivote = 0 # corresponde al pivote, que puede ser el último elemento del array

print "ANTES: ",misNumerosID
# print "Longitud del elemento: ",str(len(misNumerosID))
# print "Rango negativo: ",str(range(len(misNumerosID),0,-1))

for i in range(indice,-1,-1): # desde el último índice, al 0 (límite inferior -1), hacia atrás, de uno en uno
	for j in range(1,i+1): # desde la segunda posición [1] hasta el último índice. Límite superior i+1
		if misNumerosID[j]>misNumerosID[j-1]: # LO UNICO QUE CAMBIA ES EL SIGO AQUÍ PARA HACERLO DESCENDENTE
			pivote = misNumerosID[j]
			misNumerosID[j]=misNumerosID[j-1]
			misNumerosID[j-1]=pivote
			pivote=0

print " = = = "
print "DESPUÉS: ",misNumerosID
