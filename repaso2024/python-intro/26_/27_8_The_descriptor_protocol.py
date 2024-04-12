# El protocolo DESCRIPTOR permite hacer un seguimiento de los atributos definidos en otra clase.
# Son atributos administrados (managed atributes). En este ejemplo, el protocolo DESCRIPTOR es
# la clase LOGGER

class Logger(object):
    """ Logger class implementing the descriptor protocol"""

    def __init__(self, name):
        self.name = name

    def __get__(self, inst, owner):
        print('__get__:', inst, 'owner', owner,', value', self.name, '=', str(inst.__dict__[self.name]))
        return inst.__dict__[self.name]

    def __set__(self, inst, value):
        print('__set__:', inst, '-', self.name, '=', value)
        inst.__dict__[self.name] = value

    def __delete__(self, instance):
        print('__delete__', instance)

    def __set_name__(self, owner, name):
        print('__set_name__', 'owner', owner, 'setting', name)


class Cursor(object):
    # Set up the descriptors at the class level
    x = Logger('x')
    y = Logger('y')

    def __init__(self, x0, y0):
        # Initialise the attributes
        # Note use of __dict__ to avoid using self.x notation
        # which would invoke the descriptor behaviour
        self.__dict__['x'] = x0
        self.__dict__['y'] = y0
        # self.x = x0 daría error porque ya están creados.

    def move_by(self, dx, dy):
        print('move_by', dx, ',', dy)
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return 'Point[' + str(self.__dict__['x']) + ', ' + str(self.__dict__['y']) + ']'
        # return 'Point[' + str(self.x) + ', ' + str(self.y) + ']'


""" Programa Principal """
cursor = Cursor(15, 15)
print('-' * 25)
print('p1:', cursor)
cursor.x = 20
cursor.y = 35
print('p1 updated:', cursor)
print('p1.x:', cursor.x)
print('-' * 25)
cursor.move_by(1, 1)
print('-' * 25)
