# Clase que representa la cuenta de un banco

class Cuenta:
    """ Esta clase representa la cuenta bancaria de una persona """

    def __init__(self, num, propietario, inicial, tipo):
        self.num = num
        self.propietario = propietario
        self.balance = inicial
        self.tipo = tipo

    def ingresar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad

    def saldo(self):
        return self.balance

    def __str__(self):
        return "Cuenta[{}] de {}, del tipo {}, saldo: {}€".format(self.num, self.propietario, self.tipo, self.balance)


""" Programa Principal
    ================== """
""" Definición de cuentas """
acc1 = Cuenta('123', 'Aurelio', 10.05, 'corriente')
acc2 = Cuenta('345', 'Luis', 23.55, 'ahorros')
acc3 = Cuenta('567', 'Phoebe', 12.45, 'inversión')

print(acc1)
print(acc2)
print(acc3)

""" Aurelio hace un ingreso """
ingreso = 10000
acc1.ingresar(ingreso)
print(acc1)
cobro = 2501
acc1.retirar(cobro)
print(acc1)
print("El balance para la cuenta {} de {} es de {}€".format(acc1.num,acc1.propietario,acc1.balance))

