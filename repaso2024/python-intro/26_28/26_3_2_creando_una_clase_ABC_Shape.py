# creamos una clase del tipo ABC usando el módulo abc e importando la clase
# ABCMeta. Debo además especificar el atributo metaclass

from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, id2):
        self._id = id2

    @abstractmethod
    def display(self): pass

    @property
    @abstractmethod
    def id(self): pass


class Circle(Shape):
    """ Usamos la clase abstracta shape para definir ahora una clase concreta Circle"""
    def __init__(self, id2):
        super().__init__(id2)

    def display(self):
        print('Circle: ', self._id)

    @property
    def id(self):
        """ the id property """
        return self._id

    @id.setter
    def id(self,value):
        self._id=value


c1 = Circle(3)
c1.display()
print(c1.id)

c1.id = 45
c1.display()
