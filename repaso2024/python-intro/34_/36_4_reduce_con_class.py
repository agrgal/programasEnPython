# Uso de la función de alto nivel reduce

from functools import reduce
class Person():

    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad

    def __str__(self):
        return "(" + self.name + ", " + str(self.age) + ")"


personas = [Person("Luis", 23), Person("Alberto", 19), Person("Ana", 57)]

total_edad = reduce(lambda total, p: total + p.age, personas, 0) # necesita el valor inicial 0 ¿¿??
promedio = total_edad // len(personas)
print("La edad promedio es: ",promedio)