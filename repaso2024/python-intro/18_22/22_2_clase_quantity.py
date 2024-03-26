# como implementar el operator overload

class Cantidad:
    """ Tal como está definida, la clase es INMUTABLE, es decir, no se alteran los objetos
    iniciales. Al sumar o restar se crea un nuevo elemento, y no se alteran los originales"""
    contador = 0

    @classmethod
    def contar(cls):
        cls.contador += 1
        return cls.contador

    def __init__(self, valor):
        self.valor = valor
        self.orden = Cantidad.contar()

    def __str__(self):
        return "El valor de la cantidad [{}] es: {}".format(self.orden, self.valor)

    def __add__(self, other):
        """ Estamos tomando un valor que es la suma del primer objeto y del segundo objeto
        (de sus atributos valor) y CREANDO un tercer elemento de la misma clase. """
        nuevo = self.valor + other.valor
        return Cantidad(nuevo)

    def __sub__(self, other):
        nuevo = self.valor - other.valor
        return Cantidad(nuevo)

    def __mul__(self, other):
        """ Con la opción isinstance puedo distinguir si estoy multiplicando por un objeto
        o por una constante (que es un entero) y actuar en consecuencia"""
        if isinstance(other, int):
            nuevo = self.valor * other
        else:
            nuevo = self.valor * other.valor
        return Cantidad(nuevo)

    def __truediv__(self, other):
        """ Con la opción isinstance puedo distinguir si estoy dividiendo por un objeto
        o por una constante (que es un entero) y actuar en consecuencia"""
        if isinstance(other, int):
            nuevo = self.valor / other
        else:
            nuevo = self.valor / other.valor
        return Cantidad(nuevo)

    def __floordiv__(self, other):
        nuevo = self.valor // other.valor
        return Cantidad(nuevo)

    def __pow__(self, other):
        nuevo = self.valor ** other.valor
        return Cantidad(nuevo)

    def __mod__(self, other):
        nuevo = self.valor % other.valor
        return Cantidad(nuevo)

    def __eq__(self, other):
        return self.valor == other.valor

    def __ne__(self, other):
        return self.valor != other.valor

    def __ge__(self, other):
        return self.valor >= other.valor

    def __gt__(self, other):
        return self.valor > other.valor

    def __lt__(self, other):
        return self.valor < other.valor

    def __le__(self, other):
        return self.valor <= other.valor


""" Programa principal """

p1 = Cantidad(25)
p2 = Cantidad(13)
p3 = p1 + p2
p4 = p1 - p2
p5 = p1 * p2
p6 = p1 / p2
p7 = p1 // p2
p8 = p1 ** p2
p9 = p1 % p2
p10 = p1 * 3
p11 = p1 / 3
print(p1)
print(p2)
print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
print(p8)
print(p9)
print(p10)
print(p11)

print(p1 > p2)
print(p9 >= p8)
