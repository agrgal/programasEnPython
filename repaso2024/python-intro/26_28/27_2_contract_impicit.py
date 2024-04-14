# Contrato implícito. si en una clase hay una operación numérica
# La suma, por ejmeplo, cualquier objeto que soporte dicha operación podrá usar esa clase

class Quantity:

    def __init__(self, numero):
        self.numero = numero

    def __add__(self, other):
        return Quantity(self.numero + other.numero)

    def __str__(self):
        return "Cantidad: ["+ str(self.numero) +"]"

class Calculator:

    def add(self,x,y):
        return x+y


q1 = Quantity(3)
q2 = Quantity(7)

# print(q1+q2)

calc = Calculator()
print(calc.add(q1,q2))