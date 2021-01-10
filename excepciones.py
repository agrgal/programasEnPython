# coding: utf-8


def lee_entero():
    """ Solicita un valor entero y lo devuelve.
        Mientras el valor ingresado no sea entero, vuelve a solicitarlo. """
    while True:
        valor = raw_input("Ingrese un número: ")
        try:
            valor = int(valor)
            return valor
        except ValueError:
            try:
                valor = float(valor)
                return valor
            except ValueError:
                print "ATENCIÓN: Debe ingresar un número."

lee_entero()