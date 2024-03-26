# Defino la clase person. Con datos privados y funciones setter y getter

class Person:
    """ Esta clase representa a una persona """

    def __init__(self, name, age):
        """ Definición de atributos. CONSTRUCTOR"""
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, nombre):
        self._name = nombre

    @property
    def edad(self):
        return self._age

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and 0 < valor <= 120:
            self._age = valor
        else:
            print("Edad no válida. No se modifica")

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self._name + ' tiene ' + str(self._age) + " años"


""" Programa principal
    ================== """

p1 = Person("Ana", 45)
p2 = Person("Luis", 83)

p1.age = -5
print(p1)
