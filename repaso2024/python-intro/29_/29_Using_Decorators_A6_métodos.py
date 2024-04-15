def pretty_print(method):
    def method_wrapper(self):
        return "<p>{0}</p>".format(method(self))

    return method_wrapper


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def print_self(self):
        print('Person - ', self.name, ', ', self.age)

    @pretty_print
    def get_fullname(self):
        return self.name + " " + self.surname


p1 = Person("Aurelio", "Gallardo", 53)
print(p1.get_fullname())
