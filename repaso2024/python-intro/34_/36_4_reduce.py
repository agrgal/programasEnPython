# Uso de la función de alto nivel reduce

from functools import reduce

datos = [i for i in range(1,101)]
print(datos)

suma = reduce(lambda total, x: total+x, datos)
print(suma)