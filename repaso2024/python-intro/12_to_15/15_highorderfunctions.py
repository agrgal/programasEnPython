# Funciones de alto nivel

def mensaje(msg):    # function header
    msg = "*** "+msg+" ***"
    return msg       # function body


def mensaje2(msg):    # function header
    msg = "=== "+msg+" ==="
    return msg       # function body


print(mensaje("Hola Mundo"))   # imprime el mensaje
print(mensaje)    # sin paréntesis, implica la posición de memoria donde se empieza ejecutar la función
# Esta llamada trata a la función como un objeto. De hecho...
print(type(mensaje))   # imprimirá la clase function

otra_referencia = mensaje  # en la variable otra_referencia asigno la referencia a la función mensaje.
# De esta manera, la misma función tiene dos variables referenciadas.
print(otra_referencia("Otra frase"))

#  También podría tener un segundo mensaje, y reasignarlo a la referencia original
print(mensaje("Mensaje con la referencia a la función SIN CAMBIAR"))
mensaje = mensaje2
print(mensaje("Mensaje con la referencia a la función CAMBIADA"))