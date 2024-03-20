# Funciones de alto nivel

def mif(s):
    """ Elige tipo de función"""
    if s == "doble":
        return lambda n: 2 * n
    elif s == "triple":
        return lambda n: 3 * n
    elif s == "raíz":
        return lambda n: n ** 0.5
    elif s == "primo":
        def esprimo(num, b=2):
            if num <= 2 or (2 < num <= b):
                # si el número es 2 ó 1, o b es mayor que el número, siendo éste mayor que 2
                # devuelve True
                return True
            elif num > 2 and b < num:  # mientras que no sea False, recursivamente calcula a
                # y siempre que sea False, ya se corta, pero... ¿Por qué? ¿¿??
                # print(num % b > 0, b)
                a = (num % b > 0) and esprimo(num, b + 1)
                return a
            return True

        return esprimo

    elif s == "entero":
        def check_number(ss):
            return ss.isnumeric()

        return check_number

    else:
        raise ValueError("Función desconocida")


def aplicar(x, ff):
    """ Función que aplica una función dada"""
    return ff(x)


#  Programa principal
print(3, aplicar(3, mif("doble")))
print(3, aplicar(3, mif("triple")))
print(19, aplicar(19, mif("primo")))
print(20, aplicar(20, mif("primo")))
print("A", aplicar("A", mif("entero")))
print("4", aplicar("4", mif("entero")))
