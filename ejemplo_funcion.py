# *-* coding: utf-8 *-*
miNumero = int(raw_input("Dime un numero del 2 al 10: "))
miNumero2 = int(raw_input("Dime un numero del 2 al 10: "))


def suma(a, b):
    return a + b

for i in xrange(1, miNumero + 1):
    for j in xrange(1, miNumero2 + 1):
        print ("La suma de: " + str(i) + " y " + str(j) + " = " + str(suma(i, j)))
