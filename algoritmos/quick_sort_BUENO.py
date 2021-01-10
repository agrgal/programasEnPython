# *-* coding: utf-8 *-*

import random

def quicksort(L, first, last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last    
    pivote = (L[i] + L[j]) / 2
    print "PIVOTE: ",str(pivote)

    # iteramos hasta que i no sea menor que j
    while i < j:
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while L[i] < pivote:
            # Incrementamos el índice
            i+=1
            print "i: ",str(i)
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while L[j] > pivote:
            # decrementamos el índice
            j-=1
            print "j: ",str(j)
        # si i es menor o igual que j significa que los índices se han cruzado
        print "i: ",str(i), ", j: ",str(j), " --> números: ", L
        if i<=j:
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1
        print "L cambiado: ",L,"añadidos i e j: ",str(i),",",str(j)

    # si first es menor que j mantenemos la recursividad
    # if first < j:
    #    L = quicksort(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    # if last > i:
    #    L = quicksort(L, i, last)

    # devolvemos la lista ordenada
    return L
    

# Genero un vector con 100 elementos colocados en posiciones aleatorias
"""
misNumeros = []
for i in range(1,11):
	longitud = len(misNumeros)
	misNumeros.insert(random.randint(0,longitud),i)"""
	
misNumeros = [8,4,7,5,3,2,1,6]

print "Mis números: ",misNumeros
print "= = = "
print quicksort(misNumeros,0,len(misNumeros)-1)
