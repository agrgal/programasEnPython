# Defino la clase person

class Person:
    """ Esta clase representa a una persona """

    def __init__(self, name, age):
        """ Definición de atributos. CONSTRUCTOR"""
        self.name = name
        self.age = age

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self.name + ' tiene ' + str(self.age) + " años"

    def cumple(self):
        print("¡Felicidades! Hoy es tu cumpleaños")
        print("Tenías {antes} años, y ahora cumples {ahora}".format(antes=self.age, ahora=self.age + 1))
        self.age += 1  # Actualizo la información de la edad

    def pagos_segue_horas(self, horas_trabajadas):
        pagar_la_hora_a = 30
        if self.age >= 18:
            pagar_la_hora_a += 10  # si es mayor de 18 años, pagarlas a 10 € más cara
        return pagar_la_hora_a * horas_trabajadas

    def es_mayor_de_edad(self):
        return self.age >= 18


class Empleado(Person):

    def __init__(self, nombre, edad, Id):
        """ CONSTRUCTOR de la clase Empleado."""
        super().__init__(nombre, edad)  # Forma de llamar a inicialización de la clase Person. Poner siempre al
        # principio
        self.id = Id  # Atributo de clase nuevo

    def calcular_paga(self, horas_trabajadas):
        rate = 7.5
        if self.age > 18:
            rate += 2.5
        return rate * horas_trabajadas

    def __str__(self):
        """ Método por defecto de imprimir el objeto.
        La clase <<Empleado>> OVERRIDE el método de impresión ya definido por Person"""
        return self.name + ' (' + str(self.id) + ') tiene ' + str(self.age) + " años"


class Vendedor(Empleado):
    """ Subclass e de Empleado (a su vez de Person) que define los vendedores"""

    def __init__(self, nombre, edad, Id, ventas, region):
        super().__init__(nombre, edad, Id)
        self.ventas = ventas
        self.region = region

    def bonus(self):
        return self.ventas * 0.5

    def __str__(self):
        """ Método por defecto de imprimir el objeto.
        La clase <<Vendedor>> OVERRIDE el método de impresión ya definido por Empleado"""
        # return (self.name + ' (' + str(self.id) + ') tiene ' + str(self.age)
        #         + " años" + " y lleva la zona de "+self.region)
        return super().__str__()+" y lleva la zona de "+self.region
        # mejor se usa la extensión de los métodos de los padres.

""" ==================
    Programa Principal
    ================== """

e1 = Empleado("Aurelio", 53, 1)
e2 = Empleado("Luis", 17, 2)
v1 = Vendedor("Ana", 32, 3, 300, "Andalucía")
print(e1)
print(e2)
print(v1)

horas = 40
print("{} ha ganado {}€ por {} de trabajo".format(e1.name, e1.calcular_paga(horas), horas))
print("{} ha ganado {}€ por {} de trabajo".format(e2.name, e2.calcular_paga(horas), horas))
print("{} ha ganado {}€ por {} de trabajo más un bonus de {}€".format(v1.name, v1.calcular_paga(horas), horas,
                                                                      v1.bonus()))
