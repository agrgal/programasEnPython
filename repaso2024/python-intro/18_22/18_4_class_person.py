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

""" El identificador es único  """
print("id(p1): " + str(id(p1)))  # Identificador de la instancia u objeto p1
print("id(p2): " + str(id(p2)))  # Identificador de la instancia u objeto p2

""" Apuntando dos variables al mismo identificador """
px = p1
print("id(px): " + str(id(px)))  # Identificador de la instancia u objeto px
print("id(p1): " + str(id(p1)))  # Identificador de la instancia u objeto p1

""" Imprimir directamente p1 y p2"""
print(p1)
print(p2)  # Un poco raro, a menos que defina el método por defecto __str__

""" Imprimiendo sus atributos """
print(p1.name, 'tiene la edad de', p1.age)
print(p2.name, 'tiene la edad de', p2.age)

""" Imprimiendo la información docstring de la clase"""
print(p1.__doc__)

""" Cumpleaños"""
print(p1.name, 'tiene la edad de', p1.age)
p1.cumple()
print(p1.name, 'tiene la edad de', p1.age)

""" Pagar las horas """
print("A {nombre} hay que pagarle 40 horas: {dinero}. Es mayor de edad? {me}"
      .format(nombre=p1.name, dinero=p1.pagos_segue_horas(40), me=p1.es_mayor_de_edad()))
p3 = Person("Ana", 17)
print("A {nombre} hay que pagarle 40 horas: {dinero}. Es mayor de edad? {me}"
      .format(nombre=p3.name, dinero=p3.pagos_segue_horas(40), me=p3.es_mayor_de_edad()))

""" Borrado de objetos """
del p1  # borramos el objeto p1
# print(p1)  # incluso da un error porque ya el debugger detecta que se ha borrado.
""" Python puede gestionar la memoria, al crear y borrar objetos, lo cual es una ventaja
ante lenguajes como C o C++ donde el programador es quien debe hacerlo. Y eso no es sencillo."""
""" De hecho, Python provee un sistema de manejo de memoria que incluso cuando ésta se queda 
corta, puede borrar parte de la que ya no se está usando. Ese proceso se llama 'Recogida de basura' 
o GARBAGE COLLECTION """

""" Atributos intrínsecos """
print('Class attributes')
print(Person.__name__)
print(Person.__module__)
print(Person.__doc__)
print(Person.__dict__)
print('Object attributes')
print(p2.__class__)
print(p2.__dict__)
