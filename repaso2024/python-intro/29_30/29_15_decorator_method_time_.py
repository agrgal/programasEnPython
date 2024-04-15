# función decoradora que coge un método de la clase person e intenta averiguar
# cuánto tiempo tarda en ejecutarse

def medir(method):

    from timeit import default_timer

    def mi_tiempo(self):
        start = default_timer()
        cadena = method(self)
        end = default_timer()
        print("Empieza a: {} // {} // Termina a: {} // Diferencia {}".format(start,cadena,end,end-start))

    return mi_tiempo


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    @medir
    def print_self(self):
        return 'Person - ', self.name, ', ', self.age


p1 = Person("Aurelio", "Gallardo", 53)
p1.print_self()
