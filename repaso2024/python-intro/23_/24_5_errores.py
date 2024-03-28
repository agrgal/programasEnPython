# manejando errores. Básico

def runcalc(x):
    """Esta función dará como resultado una excepción del tipo división entre cero"""
    return x/0


try:
    runcalc(6)
    # runcalc("A")
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
