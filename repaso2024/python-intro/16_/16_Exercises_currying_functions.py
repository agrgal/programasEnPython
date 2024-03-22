# Ejercicios de conversión con funciones currying
# tasa de conversión

def tasa_conversion(cantidad, moneda_dollar):
    """ retorna la tasa de conversión de cierta cantidad
    conociendo su equivalencia en dólares"""
    return cantidad * moneda_dollar


def mi_tasa(factor):
    return lambda n: tasa_conversion(n, factor)


euro = mi_tasa(1.2)
libras = mi_tasa(2)
yenes = mi_tasa(300)

cash = int(input("Introduce la cantidad a convertir: "))
print("La cantidad de {} dólares en euros es {} €".format(cash, euro(cash)))
print("La cantidad de {} dólares en libras es {} libras".format(cash, libras(cash)))
print("La cantidad de {} dólares en yenes es {} yenes".format(cash, yenes(cash)))
