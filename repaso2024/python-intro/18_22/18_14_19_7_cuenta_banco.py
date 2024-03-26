# Clase que representa la cuenta de un banco

class Cuenta:
    """ Esta clase representa la cuenta bancaria de una persona """
    contador = 0  # creo la variable «contador» que lleva el registro de cuentas creadas
    # es una variable de clase (class side data)

    @classmethod
    def cuentas_creadas(cls):
        """ Este método de clase añade uno al contador y devuelve ese valor. Será modificado
            cada vez que se instancia o crea un objeto"""
        Cuenta.contador += 1
        return Cuenta.contador

    def __init__(self, num, propietario, inicial, tipo):
        self.num = num
        self.propietario = propietario
        self.balance = inicial
        self.tipo = tipo
        print("Cuenta nº {} creada".format(Cuenta.cuentas_creadas()))

    def __del__(self):
        """ Cuando se borra una cuenta hay que decrementar el contador"""
        if Cuenta.contador > 1:
            print("Se ha borrado una cuenta")
            Cuenta.contador -= 1

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
print("El balance para la cuenta {} de {} es de {}€".format(acc1.num, acc1.propietario, acc1.balance))

print("Actualmente en mis datos hay {} cuentas".format(Cuenta.contador))
del acc3
print("Actualmente en mis datos hay {} cuentas".format(Cuenta.contador))
print(Cuenta.__module__)