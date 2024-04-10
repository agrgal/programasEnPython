# Ejemplo con clase abstracta

from _collections_abc import MutableSequence


class Bag(MutableSequence):
    pass

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass

    def __len__(self):
        pass

    def __delitem__(self, key):
        pass

    def insert(self, index, value):
        pass


b1 = Bag()

# Aunque no he dado funcionalidad a cada método, los he definido. La clase Bag sigue
# el esquema de la clase abstracta. Ya no dará el error.
