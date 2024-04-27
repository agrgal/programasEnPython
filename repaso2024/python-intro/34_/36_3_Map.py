# defino una función map
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(datos)

d1 = list(map(lambda x: 3*x+1, datos)) # Esta función multiplica por 3 y suma 1
print(d1)

d2= list(map(lambda x, y: 5*y-3*x, datos,d1))
print(d2) # map con más de un parámetro