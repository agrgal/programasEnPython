#  Funciones que son parámetros de otras funciones

def aplicar_tasa(x, mi_funcion):
    """ Función principal de orden superior"""
    return mi_funcion(x)


def mi_tasa(x):
    """ aplico una tasa"""
    return x * 0.3 + 10


def gob_tasa(x):
    """ aplico una segunda tasa """
    return x * 0.45 - 10


ganancia = 30000
print(aplicar_tasa(ganancia, mi_tasa))   # llamo a la función de orden superior y le digo que función quiero implementar
print(aplicar_tasa(ganancia, gob_tasa))
# Las funciones de orden superior escriben un código claro cuando no sé aún la función exacta a aplicar.
# Siempre puedo, simplemente, cambiar la función a aplicar en la de orden superior.
