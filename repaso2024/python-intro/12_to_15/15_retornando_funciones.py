# Retorno de funciones

def comprobar(s):
    if s == "par":
        return lambda n: n % 2 == 0
    elif s == "positivo":
        return lambda n: n >= 0
    elif s == "negativo":
        return lambda n: n < 0
    else:
        raise ValueError("Objeto desconocido")


def sumando():
    def suma(x, y):
        return x + y

    return suma

# asignamos a variables distintas funciones lambda retornadas
f1 = comprobar("par")  # función par
f2 = comprobar("positivo")  # función positivo
print(f1(3), f2(3))

# asignamos a variable una función definida con nombre
ff = sumando() # asigna a ff la función suma
print (ff(4,5))
