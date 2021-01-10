# *-* coding:utf-8 *-*

# Validaciones
def es_numero(num):
    # indica si es o no un valor numérico
    return isinstance (num, (int, float, complex, long))

# clase puntos
class punto(object):
    """ Clase que permite trabajar con puntos en el plano,
    en coordenadas cartesianas, x e y"""

    def __init__(self, x0=0.0, y0=0.0):
        """ pre: los puntos deben definirse con sus coordenadas x
        e y - tipo float - y pueden establecerse en la llamada inicial.
        La notación superior x0=0.0 e y0=0.0 indica los valores iniciales
        si no se define en la llamada """
        if es_numero(x0) and es_numero(y0):
            self.x = x0
            self.y = y0
        else:
            raise TypeError("x e y deben ser números")

    def imprimir(self):
        print("[%.2f, %.2f]") % (self.x, self.y)

# Programa principal
# Punto A, # Defino valores al principio
A = punto(6,7)

# Punto B. Sin definir valores al principio.
B = punto(2,2)

# Imprime los puntos
A.imprimir()
B.imprimir()
