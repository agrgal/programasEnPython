# ejemplo del módulo collections

import collections

frutas = collections.Counter(['manzana','plátano','fresa','manzana','fresa','fresa','pera'])
print(frutas)
print(frutas['fresa'])

print(frutas.most_common(1))  # obtiene el elemento más común

frutas['plátano'] += 5  # añade 5 plátanos más

print(frutas)

print(frutas.most_common(1))  # obtiene el elemento más común