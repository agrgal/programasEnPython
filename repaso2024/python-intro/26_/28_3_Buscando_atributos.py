# Tenemos una clase estudiante, que define instancias alumnos

class Estudiante:
    count = 0  # atributo de clase

    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        Estudiante.count += 1

    def __str__(self):
        return self.nombre + " pertenece al curso " + self.curso


""" Programa principal """

a1 = Estudiante("Luis", "1ESOC")
print("Atributos de clase: ", Estudiante.__dict__)
print("Atributos de instancia u objeto: ", a1.__dict__)
