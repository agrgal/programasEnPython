# Defino la clase person

class Person:
    """ Esta clase representa a una persona.
     Añado una variable de clase, número de personas"""
    num_of_persons = 0  # esta es una variable de clase, que no pertenece a ninguna instancia

    @classmethod
    def increment_num_person(cls):
        """ Es un método de clase. Se pone la palabra reservada @classmethod
            la autollamada a la clase se hace con cls """
        cls.num_of_persons +=1

    @staticmethod
    def static_function():
        """ Son funciones independientes dentro de una clase. Se llamaría con
        Person.static_function()"""
        print("Esto es una función estática")

    def __init__(self, name, age):
        """ Definición de atributos. CONSTRUCTOR"""
        self.name = name
        self.age = age
        # Person.num_of_persons +=1 # variable de la clase que va contando el número de personas
        Person.increment_num_person()  # o bien lo hago con un método de clase

    def __str__(self):
        """ Método por defecto de imprimir el objeto """
        return self.name + ' tiene ' + str(self.age) + " años"

    def cumple(self):
        print("¡Felicidades! Hoy es tu cumpleaños")
        print("Tenías {antes} años, y ahora cumples {ahora}".format(antes=self.age, ahora=self.age + 1))
        self.age += 1  # Actualizo la información de la edad

    def pagos_segue_horas(self, horas):
        pagar_la_hora_a = 30
        if self.age >= 18:
            pagar_la_hora_a += 10  # si es mayor de 18 años, pagarlas a 10 € más cara
        return pagar_la_hora_a * horas

    def es_mayor_de_edad(self):
        return self.age >= 18


""" ==================
    Programa Principal
    ================== """

p1 = Person("Aurelio", 53)  # Definición de una instancia
p2 = Person(name="Julio", age=45)  # Definición de otra instancia
print(p1)
print(p2)
print("Número de personas: {}".format(Person.num_of_persons))
Person.static_function()
