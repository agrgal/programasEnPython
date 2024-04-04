# Defino la clase person. Con datos privados y funciones setter y getter
# Y además una excepción pèrsonalizada

class InvalidAgeException(Exception):
    """Subclase personalizada de la clase exception"""

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Edad no válida. Se provoca una excepción:" + str(self.valor)


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

    @name.deleter  # le defino un deleter.
    def name(self):
        pass

    @property
    def age(self):
        """ Esta propiedad almacena la edad """  # actúa como 'doc' de la propiedad
        return self._age

    @age.setter
    def age(self, valor):
        """ Este es el setter. Se escribe IGUAL pero con la propiedad @edad.setter"""
        if isinstance(valor, int) and 0 < valor <= 120:
            self._age = valor
        else:
            # print("Edad no válida. No se modifica")
            raise InvalidAgeException(valor)

    @age.deleter
    def age(self):
        """ Este es el deleter. Se escribe IGUAL pero con la propiedad @edad.deleter"""
        pass

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self._name + ' tiene ' + str(self._age) + " años"


""" Programa principal
    ================== """

try:
    p1 = Person("Ana", 45)
    p2 = Person("Luis", 83)
    p1.age = -56
    print(p1)
except InvalidAgeException as iae:
    print("Aquí se ha introducido una edad incorrecta")
    print(iae)  # Se recupera lo que se ha programado en el __str__ de la subclase Exception
