# Añadir funcionalidad en tiempo de ejecución

class Bag:
    def __init__(self):
        self.data = ['a', 'b', 'c']

    def __getitem__(self, pos):
        return self.data[pos]

    def __str__(self):
        return 'Bag(' + str(self.data) + ')'


def getlength(self):
    return len(self.data)


# Monkey patching
Bag.__len__ = getlength
Bag.name = "mi bolsa"
b = Bag()
print(b)
print(b.name)

b.name = "mi nueva bolsa"
print(b.name)

# pero no podemos hacer
print(len(b))


