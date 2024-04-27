# probando el módulo Counters

import collections

cadena = input("Introduce alguna frase: ")  # Introduzco una cadena
palabras = sorted(cadena.lower().split(" ")) # divido la cadena por los espacios; obtengo las palabras

print("Palabras ordenadas")
print(palabras)

mispalabras = collections.Counter(palabras)
mispalabrasordenadas = collections.OrderedDict(mispalabras)   #  objeto counter admite

print("Objeto counter, desordenado")
print(mispalabras)

print("Objeto orderedDict, ordenado")
print(mispalabrasordenadas)
