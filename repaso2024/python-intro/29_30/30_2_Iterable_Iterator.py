# clase que define un método iter (iterable)
# y un método next() iterador

class Evens:
    """clase que genera números pares"""

    def __init__(self, limit):
        self.limit = limit
        self.val = 0

    def __iter__(self):
        """ Hago esta clase iterable"""
        return self

    def __next__(self):
        """ Iterador. Si el valor es mayor que el límite, que genere una excepción"""
        if self.val > self.limit:
            raise StopIteration
        else:
            valor = self.val
            self.val += 2
            return valor

print('Start')
for i in Evens(8):
    print(i, end=', ')
print("Hecho")
