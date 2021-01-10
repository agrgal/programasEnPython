# *-* coding: utf-8 *-*

import random

# =============================================================
# ALGORITMO DE ORDENACION POR INSERCIÓN DIRECTA
# =============================================================

# Genero un vector con 100 elementos colocados en posiciones aleatorias
misNumeros = []
for i in range(1,11):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)

# print misNumeros

# =========================
# Ordenacion por quick sort
# =========================

misNumerosID = misNumeros[:] #COPIO los valores del array
indice=len(misNumerosID)-1 # corresponde a la última posición del array
valorMuestra = misNumerosID[indice]

print "ANTES: ",misNumerosID
# print "Longitud del elemento: ",str(len(misNumerosID))
# print "Rango negativo: ",str(range(len(misNumerosID),0,-1))

print valorMuestra

temporal = 0
inf=0
sup=indice
cont = 1

def ordenarLista(listado,inferior,superior):
	temporal = 0
	cont =1
	i=inferior
	j=superior-1
	while (listado[i]>listado[superior]):
		while(listado[j]<listado[


print " = = = "
print "DESPUÉS: ",misNumerosID
