frutas = {'pera', 'fresa', 'manzana'}
print(frutas)

frutas2 = {'pera', 'fresa', 'manzana', 'pera', 'fresa'}
print(frutas2)  # no permite duplicados. Elimina los que están duplicados.

tuple1 = (5, 6, 7, 8, 9, 6, 7, 3)
set2 = set(tuple1)  # la orden set permite convertir un iterable en un set.
print(set2)

# Comprobando si en un set hay algo. Palabra reservada "in"
print ('pera' in frutas)

# Añadiendo datos al set
frutas.add("naranja")
frutas.update(["ciruelas","mandarinas"]) # con el método update
print(frutas)

print(len(frutas))
print(min(frutas))  # lo que no le veo la lógica, a menos que sea orden alfabético, es con strings.
print(max(frutas))

frutas2.discard("manzana")
frutas2.pop()
print(frutas2)
frutas2.clear()
print(frutas2)