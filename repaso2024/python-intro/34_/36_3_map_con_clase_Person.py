class Person():

    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad

    def __str__(self):
        return "(" + self.name + ", " + str(self.age) + ")"


# Map con la clase Person
personas = [Person("Luis", 23), Person("Alberto", 19), Person("Ana", 57)]

for p in personas:
    print(p, end=" // ")

edades = list(map(lambda p: p.age, personas ))
print(edades) # imprime las edades de esas personas