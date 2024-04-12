# Duck Typing. Aquello que cumpla con el contrato implícito puede
# usarse. Por ejemplo, como Distancias pueden sumarse y restarse
# podrán usar los métodos de calculator add y subtract pero no los de multiplicar
# y dividir

class Distance:

    def __init__(self, d):
        self.value = d

    def __add__(self, other):
        return Distance(self.value + other.value)

    def __sub__(self, other):
        return Distance(self.value - other.value)

    def __str__(self):
        return "Distancia: [" + str(self.value) + "]"


class Calculator:

    def suma(self, x, y):
        return x + y

    def resta(self, x, y):
        return x - y

    def mult(self, x, y):
        return x * y

    def dividir(self, x, y):
        return x / y


d1 = Distance(3)
d2 = Distance(7)

calc = Calculator()
print(calc.suma(d1, d2))
print(calc.resta(d1,d2))
# print(calc.mult(d1.d2)) --> daría un error, porque no cumple el contrato implícito.
