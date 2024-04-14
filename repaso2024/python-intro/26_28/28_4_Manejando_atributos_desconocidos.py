# Tenemos una clase estudiante, que define instancias alumnos

class Estudiante:
    count = 0  # atributo de clase

    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        Estudiante.count += 1

    def mymethod(self):
        return 'default'

    def __getattr__(self, item):
        print("No he encontrado el atributo: ",item)
        return self.mymethod()

    def __getattribute__(self, item):
        print ("Has llamado a un atributo ", item)
        return object.__getattribute__(self,item)

    def __setattr__(self, key, value):
        print("He cambiado el atributo "+key+" con el valor "+value)
        # self.__dict__[key]=value
        object.__setattr__(self,key,value)

    def __str__(self):
        return self.nombre + " pertenece al curso " + self.curso


""" Programa principal """

a1 = Estudiante("Luis", "1ESOC")
a1.nombre = "Pepe"
print(a1)