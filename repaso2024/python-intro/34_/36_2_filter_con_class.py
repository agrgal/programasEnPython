# Defino filter para usar con una clase

class Person():

    def __init__(self, nombre, edad):
        self.name = nombre
        self.age = edad

    def __str__(self):
        return "(" + self.name + ", " + str(self.age) + ")"


personas = [Person("Luis", 23), Person("Alberto", 19), Person("Ana", 57)]

for p in personas:
    print(p, end=" // ")

print()
print("="*25)

jovenes = filter(lambda p: p.age <= 30, personas)
for p in jovenes:
    print(p, end=" // ")
