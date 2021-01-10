# *-* coding:utf-8 *-*
xs = [2003, 6789, 5488, 3245]

print xs

xs[1] = 10325

print ("Cambio un elemento de la lista - índice 1: %s") % (xs)

xs.append(9999)

print ("Añado un elemento al final: %s") % (xs)

xs.insert(2, 2332)

print ("Inserto un elemento con índice 2: %s") % (xs)

xs.insert(2, 9999)

print ("Inserto un elemento con índice 2, de nuevo, el anterior pasa al 3: %s") % (xs)

xs.remove(2332)

print ("Quitar un elemento de la lista, el 2332: %s") % (xs)

xs.remove(9999)

print ("Quitar un elemento de la lista, el 9999: %s") % (xs)
print ("Si el elemento está repetido, se quita el primero de la lista ")
print ("Si intento quitar uno que no exista, da un error")

estaONo = 5488 in xs
print ("Comprobar si está o no en la lista %s") % (estaONo)

indice = xs.index(5488)
print ("Devueleve el índice o posición de un elemento, 5488: %d") % (indice)
print ("%s") % (xs)

