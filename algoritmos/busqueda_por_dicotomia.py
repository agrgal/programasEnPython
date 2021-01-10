# *-* coding: utf-8 *-*

import random

def quicksort(L, first, last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last    
    pivote = (L[i] + L[j]) / 2
    # print "PIVOTE: ",str(pivote)

    # iteramos hasta que i no sea menor que j
    while i < j:
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while L[i] < pivote:
            # Incrementamos el índice
            i+=1
            # print "i: ",str(i)
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while L[j] > pivote:
            # decrementamos el índice
            j-=1
            # print "j: ",str(j)
        # si i es menor o igual que j significa que los índices se han cruzado
        # print "i: ",str(i), ", j: ",str(j), " --> números: ", L
        if i<=j:
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1
        # print "L cambiado: ",L,"añadidos i e j: ",str(i),",",str(j)
    
    # si first es menor que j mantenemos la recursividad
    if first < j:
        L = quicksort(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if last > i:
        L = quicksort(L, i, last)

    # devolvemos la lista ordenada
    return L
    

# Función de búsqueda dicotómica
""" def busquedaDicotomica (L,aguja,desde,hasta):	
	i = (desde+hasta)/2 # valor intermedio.
	while L[i]!=aguja:
		print "Voy buscando índices...: %d --> %d" % (i,L[i])
		if L[i]>aguja: # está en el lado de valores más pequeños
			hasta = i-1
		elif L[i]<aguja: # está en el lado de valores mayores
			desde = i+1
		i = (desde+hasta)/2 # valor intermedio. Recalculo.
	return i """

# Función de búsqueda dicotómica RECURSIVA
def busquedaDicotomica (L,aguja,desde,hasta):
	ans = -1 # En principio, la respuesta es -1
	if desde>=hasta:
		ans = -1 # Si los dos índices se encuentran, o el inferior supera al superior,  es que no ha encontrado nada 
	else:
		centro = (desde+((hasta-desde)//2)) # calculo el centro... // cociente de la división
		if   aguja < L[centro]: 
			ans = busquedaDicotomica(L,aguja,desde,centro) # Busco en la parte del array inferior. No poner centro-1 ??
		elif aguja > L[centro]: 
			ans = busquedaDicotomica(L,aguja,centro+1,hasta) # busco en la parte del array superior
		else:    
			ans = centro # Y si lo encuentra, es la respuesta
	return ans 

    
# ================== 
# Programa principal
# ==================
# Genero un vector con 20 elementos colocados en posiciones aleatorias, de números entre 1 y 100

numeroDeElementos = 50
maximoNumeroAparecido = 100000
misNumeros = []
for i in range(1,maximoNumeroAparecido+1):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)
misNumeros = misNumeros[:numeroDeElementos] # solo quiero 20 números

print "Mis números: ",misNumeros
print "= = = "

print "Pero ahora los ordeno... "
misNumeros = quicksort(misNumeros,0,len(misNumeros)-1)
print "Ordenados: ",misNumeros

# ===========================================================================
# Búsqueda dicotómica
# ¿En qué lugar encuentro uno de los números?
# Uso búsqueda secuencial cuando la lista no es ordenada o no puedo ordenarla
# Método más lento. No queda más remedio que recorrer uno a uno.
# ===========================================================================

numeroAleatorio = misNumeros[random.randint(0,len(misNumeros)-1)]
# numeroAleatorio = 43
print "El número elegido es el %d" % (numeroAleatorio)

indiceEncontrado = busquedaDicotomica(misNumeros,numeroAleatorio,0,len(misNumeros)-1)

if indiceEncontrado!=-1:
	print "El valor buscado se encuentra en el lugar...: %d" % (indiceEncontrado)
	print "Compruebo... %d" % (misNumeros[indiceEncontrado])
else:
	print "No encontrado"

# print quicksort(misNumeros,0,len(misNumeros)-1)
