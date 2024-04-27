# La clase queue (cola)

class cola():

    def __init__(self):
        self._lista=[]

    def append(self,valor):
        self._lista.append(valor)

    def enqueueing(self,valor):
        # El mismo método que append, llamado enqueueing
        self._lista.append(valor)

    def __len__(self):
        return len(self._lista)
    def peek(self):
        return self._lista[0]

    def pop(self):
        first = self._lista.pop(0)
        return first

    def dequeueing(self):
        # El mismo método que pop, llamado enqueueing
        self.pop(self)

    def is_empty(self):
        return len(self._lista)==0

    def __str__(self):
        return "Mi cola es: " + str(self._lista)

# Programa principal

# A) creamos una lista
milista = cola()
print(milista)
print("¿Está vacía? ",milista.is_empty())


# B) añadimos 10 elementos
for i in range(0,9):
    milista.enqueueing(chr(i+65))

#C) imprime cola
print(milista)

#D) muestra primer elemento e imprime cola
print ("Primer elemento (sin quitar): ",milista.peek())
print(milista, "longitud: ",len(milista))

#D) muestra primer elemento e imprime cola
first = milista.pop()
print ("Primer elemento (quitándolo): ",first)
print(milista, "longitud: ",len(milista))

#E) añado el primero al final
milista.enqueueing(first)
print(milista, "longitud: ",len(milista))