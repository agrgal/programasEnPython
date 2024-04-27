# implementando una clase pilas con una lista

class Pila:

    def __init__(self):
        self._lista = []  # creo una pila vacía

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


# Programa principal

mipila = Pila()
print(mipila, "longitud: ", len(mipila))
print("¿Está vacía?", mipila.is_empty())

# B) añadimos 10 elementos
for i in range(0,20):
    mipila.push(chr(i+65))
print(mipila, "longitud: ", len(mipila))

# C) Recupero sin borrar el último elemento
print("El elemento arriba de la pila es: ",mipila.top())
print(mipila, "longitud: ", len(mipila))

# D) Recupero borrándolo el último elemento
ultimo = mipila.pop()
print("El elemento arriba de la pila es: ",ultimo)
print(mipila, "longitud: ", len(mipila))

# E) Y se lo vuelvo a añadir tuneado
mipila.push("*"+ultimo+"*")
print(mipila, "longitud: ", len(mipila))

