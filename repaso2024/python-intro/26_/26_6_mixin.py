# Uso de clases mixin (aunque son métodos concretos, son consideradas ABCs)

from abc import ABCMeta


class PrinterMixing(metaclass=ABCMeta):
    def print_me(self):
        print(self)


class Person(object):

    def __init__(self, name):
        self.name = name


class Employee(Person, PrinterMixing):

    def __init__(self, nombre, id, edad):
        super().__init__(nombre)
        self.id = id
        self.edad = edad

    def __str__(self):
        return 'Employee(' + str(self.id) + ') ' + self.name + ' [' + str(self.edad) + ']'

""" Programa Principal """

e1 = Employee("Luis", 32, 45)
e1.print_me()