# clases virtuales. Tengo dos clases como las siguientes

from abc import ABCMeta


class Person(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        print('Happy Birthday')

class Employee(object):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def birthday(self):
        print('Its your birthday')

"""
    Programa principal 
    ================== """

# Estas órdenes producen FALSE, a menos que introduzca la orden register
Person.register(Employee) # importante AHORA Employee es una subclase virtual de Person
print(issubclass(Employee,Person))
e1 = Employee("Luis",56,3)
print(isinstance(e1,Person))