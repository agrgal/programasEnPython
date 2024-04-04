# Defino la clase person. Con datos privados y funciones setter y getter

class Person:
    """ Esta clase representa a una persona """

    def __init__(self, name, age):
        """ Definición de atributos. CONSTRUCTOR"""
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_name(self, nombre):
        self._name = nombre

    def set_age(self, edad):
        if isinstance(edad, int) and 0 < edad <= 120:
            self._age = edad
        else:
            print("Edad no válida. No se modifica")

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self._name + ' tiene ' + str(self._age) + " años"

""" Programa principal
    ================== """

p1 = Person("Ana",45)
p2 = Person("Luis",83)

print(p1.get_age())
# se puede modificar, pero a tu propio riesgo
p1._age=-1
print(p1)

# Lo mejor es hacerlo mediante una función set, que compruebe si el dato es o no válido
p1.set_age(-5) # daría un aviso de edad errónea
p1.set_age(23) # esto ya sí me valdría para establecer la edad.

print(p1)
print(p2)