# -*- coding: utf-8  -*-


def dividir (dividendo, divisor):
    assert divisor !=0, "El divisor no puede ser cero"
    cociente = dividendo / divisor
    return cociente

def maximo(lista):
    """Devuelve el elemento máximo de la lista o None si estar vacía.
    Pre: lista con elementos comparables.
    Post: devuelve elemento máximo o None si la lista es vacía
    Invariable: max_elem siempre es el máximo en la iteración, de cualquier
    porción de la lista analizada
    """
    if not len(lista):
        return None
    max_elem = lista[0]
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem

lista=[0, 23, 67, 15]

print lista
print ("El máximo de la lista es %d") % (maximo(lista))

print dividir (20.12, 10)