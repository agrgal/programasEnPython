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
        self._balance = inicial
        self.tipo = tipo
        print("Cuenta nº {} creada".format(Cuenta.cuentas_creadas()))

    # def __del__(self): --> lo anulo
    #     """ Cuando se borra una cuenta hay que decrementar el contador"""
    #     if Cuenta.contador > 1:
    #        print("Se ha borrado una cuenta")
    #        Cuenta.contador -= 1

    @property
    def balance(self):
        """ BALANCE: propiedad que es capaz de almacenar el balance de una cuenta.
         Sin setter. solo READ-ONLY"""
        return self._balance

    def ingresar(self, cantidad):
        """ Sin embargo, aunque es privada conservo el método ingresar"""
        self._balance += cantidad

    def retirar(self, cantidad):
        """ Sin embargo, aunque es privada, conservo el método retirar"""
        self._balance -= cantidad

    def __str__(self):
        return "Cuenta[{}] de {}, del tipo {}, saldo: {}€".format(self.num, self.propietario, self.tipo, self._balance)


class CuentaDeposito(Cuenta):

    def __init__(self, num, propietario, inicial, interes=5):
        """ Añade tipo de interés como atributo de la  nueva cuenta de depósito"""
        super().__init__(num, propietario, inicial, tipo="ahorros")
        self.interes = interes

    def __str__(self):
        """ Utiliza parte de la cadena de la clase padre"""
        return super().__str__() + " interés: {}%".format(self.interes)


class CuentaCorriente(Cuenta):

    def __init__(self, num, propietario, inicial, limite=1000):
        """ Añade límite como atributo de la  nueva cuenta corriente"""
        super().__init__(num, propietario, inicial, tipo="corriente")
        self.limite = limite

    def __str__(self):
        """ Utiliza parte de la cadena de la clase padre"""
        return super().__str__() + " límite: {}€".format(self.limite)

    def retirar(self, cantidad):
        """ Nueva definición de retirar. Si está por debajo del límite, da un aviso."""
        if self._balance - cantidad <= self.limite:
            print("Lo siento, pero si aplico esta retirada estas por debajo del límite. Operación anulada.")
        else:
            self._balance -= cantidad


class CuentaInversion(Cuenta):

    def __init__(self, num, propietario, inicial, tipo_inversion="low"):
        """ Añade límite como atributo de la  nueva cuenta corriente"""
        super().__init__(num, propietario, inicial, tipo="inversión")
        self.tipo_inversion = tipo_inversion

    def __str__(self):
        """ Utiliza parte de la cadena de la clase padre"""
        return super().__str__() + " tipo de inversión riesgo: {}".format(self.tipo_inversion)


""" Programa Principal
    ================== """

""" Definición de cuentas """
cc1 = CuentaCorriente(1, "Aurelio", 10000, 1000)
print(cc1)
cd1 = CuentaDeposito(2, "Ana", 2000, interes=10)
print(cd1)
ci1 = CuentaInversion(3, "Luis", 2000, tipo_inversion="alto")
print(ci1)

print("Aquí no te deja hacerlo")
print("=======================")
cc1.retirar(9010)
print(cc1)
print()

print("Aquí sí te deja hacerlo")
print("=======================")
cc1.retirar(8000)
print(cc1)
print()

print("Trabajando con _balance")
print("=======================")
print("Imprimo en pantalla el balance: {}€".format(cc1.balance))
print("Intento añadirle directamente algo: COMPROBAR QUE DA ERROR")
# cc1.balance = 4000 --> daría un error porque es de solo lectura. No tengo setter asociado.
print("Pero sí puedo INGRESAR 200€")
cc1.ingresar(200)
print(cc1)
print("Y sí puedo RETIRAR 600€")
cc1.retirar(600)
print("Vuelvo a imprimir en pantalla el balance: {}€".format(cc1.balance))
