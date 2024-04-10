# Ejemplo con clase abstracta

from _collections_abc import MutableSequence


class Bag(MutableSequence):
    pass

b1=Bag()

# Esto provoca un error. La clase creada Bag tiene que
# implementar los métodos __delitem__, __getitem__, __len__, __setitem__, insert