# *-* coding: utf-8 *-*
#  Funciones

#  Factorial


def factorial(num):
    producto = 1
    for i in range(1, num + 1):
        producto = producto * i
    return producto


# Sumatorio
def sumatorio(num):
    suma = 0
    for i in range(1, num + 1):
        suma = suma + i
    return suma

""" programa principal """

n = int(raw_input("Dime un número del 1 al 100: "))

if (n < 1) or (n > 100):
    print ("Número fuera del intervalo")
    exit
else:
    print ("El factorial del número es %d y su sumatorio %d\n") % (factorial(n), sumatorio(n))
    print ("La relación factorial / sumatorio es %.3f") % (float(factorial(n)) / float(sumatorio(n)))



