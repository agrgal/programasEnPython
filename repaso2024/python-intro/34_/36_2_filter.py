# ejemplo de la función filter

def pares(x):
    return x % 2 == 0


datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(datos)

d2 = list(filter(lambda i: i % 2 == 0, datos))  # Solo encuentra los pares. Hay que convertirlo en lista
print(d2)

d3 = list(filter(pares, datos))  # Solo encuentra los pares, con una función. Hay que convertirlo en lista
print(d3)
