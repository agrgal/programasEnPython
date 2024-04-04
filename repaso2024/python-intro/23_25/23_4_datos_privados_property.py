class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    """ Me da warnings, pero funciona. Parece que el método aceptado ahora es 
    definir las propiedades mediante decoradores."""
    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )


c1 = Circle(48)

c1.radius = 67
print(c1.radius)

