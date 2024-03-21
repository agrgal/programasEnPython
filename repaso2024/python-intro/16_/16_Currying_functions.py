# Funciones tipo "currying" por Haskell Curry
# el objetivo es reusar funciones fijando algunos parámetros
# Son como funciones derivadas unas de otras.

def multiply(x, y):
    """ Esta función multiplica dos valores"""
    return x * y


def multby(func, num):
    """ Esta función toma como parámetros una función y un número
    y devuelve una nueva función con un parámetro fijado y un nuevo parámetro y
    que hay que proporcionar """
    return lambda y: func(num, y)


double = multby(multiply, 2)  # esta función resulta de asignar el número 2 como fijo en la función multiply
# pero aún debe proporcionar un número y
triple = multby(multiply, 3)

print(multiply(4, 5))
print(double(44))
print(triple(44))
