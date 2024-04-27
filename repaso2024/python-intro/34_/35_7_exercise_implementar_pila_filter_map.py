# implementando una clase pilas con una lista

class Pila:

    def __init__(self):
        self._lista = []  # creo una pila vacía

    def __iter__(self):  # nuestra pila es así un iterable.
        return iter(self._lista)

    def push(self, valor):
        self._lista.append(valor)

    def pop(self):
        mivalor = self.top()
        self._lista = self._lista[:-1]  # la lista es hasta el índice menos 1.
        return mivalor

    def top(self):
        return self._lista[-1]  # retorno el último valor

    def __len__(self):
        return len(self._lista)

    def is_empty(self):
        return len(self._lista) == 0

    def __str__(self):
        return "Mi pila es: " + str(self._lista)

    def is_letra(self, letra):
        cc = list(filter(lambda x: x == letra, self))
        return cc

    def decorar(self, caracter_decorador):
        return list(map(lambda x: caracter_decorador + x + caracter_decorador, self))


# Programa principal

mipila = Pila()
print(mipila, "longitud: ", len(mipila))
print("¿Está vacía?", mipila.is_empty())

# B) añadimos 10 elementos
for i in range(0, 20):
    mipila.push(chr(i + 65))
    mipila.push(chr(i + 65))  # duplico valores
print(mipila, "longitud: ", len(mipila))

# C) Compruebo con filter si alguna es "J"
compruebo = list(filter(lambda x: x == "J", mipila))
print("Los elementos que son 'J': ", compruebo)

# C1) Lo mismo con el método is_letra
compruebo2 = mipila.is_letra("S")
print("Los elementos que son 'S': ", compruebo2)

# D) Decora los valores con map
decorar = list(map(lambda x: "*" + x + "*", mipila))
print("Los elementos decorados son: ", decorar)

# D1) Decorar los calores con el método decorar
decorar2 = mipila.decorar(" +*+ ")
print("Los elementos decorados son: ", decorar2)
