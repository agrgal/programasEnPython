# La clase queue (cola)

class cola():

    def __init__(self):
        self.lista=[]

    def append(self,valor):
        self.lista.append(valor)

    def __len__(self):
        return len(self.lista)
    def peek(self):
        return self.lista[0]

    def pop(self):
        first = self.lista.pop(0)
        return first

    def __str__(self):
        return "Mi cola es: " + str(self.lista)
# Programa principal

# A) creamos una lista
milista = cola()

# B) añadimos 10 elementos
for i in range(0,9):
    milista.append(chr(i+65))

#C) imprime cola
print(milista)

#D) muestra primer elemento e imprime cola
print ("Primer elemento (sin quitar): ",milista.peek())
print(milista)

#D) muestra primer elemento e imprime cola
first = milista.pop()
print ("Primer elemento (quitándolo): ",first)
print(milista)