# *-* coding: utf-8 *-*
a = 3
b = 2

print (a - b == 1)
print (a - b == 2)  # comparación iguales

print (a + b != 6)  # comparación distinto

print (a > b)
print (a < b)  # mayor o menor

print (a >= 5)
print (a <= 6)  # mayor igual o menor igual

x = [1, 2, 3]
y = [1, 2, 3]

if (x == y):
    print "Valen lo mismo"

if x is y:
    print "Son el mismo objeto.Identificadores: " + str(id(x))+ " - "+str(id(y))
else:
    print "NO son el mismo objeto. Identificadores: " + str(id(x))+ " - "+str(id(y))

""" Fuerzo a que sean el mismo objeto """
x = y
if x is y:
    print "Son el mismo objeto.Identificadores: " + str(id(x))+ " - "+str(id(y))
else:
    print "NO son el mismo objeto. Identificadores: " + str(id(x))+ " - "+str(id(y))
