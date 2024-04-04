# manejando errores. Algo más

def runcalc(x, y):
    """Esta función dará como resultado una excepción del tipo división entre cero"""
    print("00>> Empezando la función... ")
    result = x / y
    print("01>> Acabando la función...")
    return result


print("EMPEZAMOS....")

try:
    print("0> Antes de la función")
    print(runcalc(6, 0))
    print("1> Después de la función")
except ZeroDivisionError as exp:
    """ Si no se escribe nada, el sistema traza el error de forma estándar"""
    """ Puede ser de la subclase ZeroDivisionError o..."""
    print(exp)
    print("Estás intentando dividir entre cero")
except Exception as eee:
    """ Esta es una forma más general. Sin embargo PyCharm me advierte que debería
    ser más específico"""
    print(eee)
    print("Error más genérico")
else:
    print("Todo fue fantástico. Me ejecuto si todo fue bien")
finally:
    print("Esto se ejecutará de cualquier forma")

print("TERMINAMOS....")
