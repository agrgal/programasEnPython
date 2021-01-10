# *-* coding:utf-8 *-*
xs = [2003, 6789, 5488, 3245]

print xs

print ("Longitud de la lista: %d") % (len(xs))

print ("Primer elemento %d") % (xs[0])
print ("Último elemento %d") % (xs[3])

print ("Sublista, del principio hasta el elemento 1 %s") % (xs[:1])
print ("Del elemento 0 al elemento 1-1, o sea, el 0")
print ("Recuerda, el orden de una lista empieza en el índice 0\n")

print ("Sublista [1:1] %s") % (xs[1:1])
print ("Recuerda, del elemento 1 al elemento 1-1=0... Inexistente\n")

print ("Sublista [1:2] %s") % (xs[1:2])
print ("Del elemento 1 al elemento 2-1, o sea, el 1. \n")

print ("Sublista [1:4] %s") % (xs[1:4])
print ("Del elemento 1 al elemento 4-1, o sea, el 3. \n")

print ("Sublista,. Menos el último [:-1] %s") % (xs[:-1])
print ("Sublista,  Menos los dos últimos [:-2] %s") % (xs[:-2])

print ("Sublista, el último [-1:] %s") % (xs[-1:])
print ("Sublista, los dos últimos [-2:] %s") % (xs[-2:])

