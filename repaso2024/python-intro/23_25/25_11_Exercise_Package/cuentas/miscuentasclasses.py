# Clase que representa la cuenta de un banco

class CantidadException(Exception):
    """ Maneja excepciones si al crear una cuenta se queda con número negativo"""

    def __init__(self, num, cantidad):
        self.num = num
        self.cantidad = cantidad

    def __str__(self):
        return "EXCEPCIÓN: La cuenta {} no puede quedarse con un saldo de {}".format(self.num, self.cantidad)


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
        if inicial >= 0:
            self._balance = inicial
        else:
            raise CantidadException(num, inicial)
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
            raise CantidadException(self.num,self._balance-cantidad)
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
