# Concatenando excepciones

class DividiendoEntreCero(Exception):
    """ Clase customizada"""

    def __str__(self):
        return "Aquí se ha dividido entre cero"


def mi_funcion(x, y):
    try:
        return x / y
    except Exception as e:
        raise DividiendoEntreCero from e  # forma de concatenar dos excepciones


def main():
    print(mi_funcion(4, 0))

main()