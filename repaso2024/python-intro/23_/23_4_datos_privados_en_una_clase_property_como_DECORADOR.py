# Defino la clase person. Con datos privados y funciones setter y getter

class Person:
    """ Esta clase representa a una persona """

    def __init__(self, name, age):
        """ Definición de atributos. CONSTRUCTOR"""
        self._name = name
        self._age = age

    @property
    def name(self):
        """ Propiedad de solo lectura que ofrece el nombre de una persona"""
        return self._name

    # @name.setter --> introducir un setter para el nombre
    # def set_name(self, nombre): --> no pongo setter
    #    self._name = nombre

    @name.deleter # le defino un deleter.
    def name(self):
        pass

    @property
    def age(self):
        """ Esta propiedad almacena la edad """  # actúa como doc de la propiedad
        return self._age

    @age.setter
    def age(self, valor):
        """ Este es el setter. Se escribe IGUAL pero con la propiedad @edad.setter"""
        if isinstance(valor, int) and 0 < valor <= 120:
            self._age = valor
        else:
            print("Edad no válida. No se modifica")

    @age.deleter
    def age(self):
        """ Este es el deleter. Se escribe IGUAL pero con la propiedad @edad.deleter"""
        pass

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self._name + ' tiene ' + str(self._age) + " años"


""" Programa principal
    ================== """

p1 = Person("Ana", 45)
p2 = Person("Luis", 83)

p1.age = -5
print(p1)

p2.age = 23
print(p2)
