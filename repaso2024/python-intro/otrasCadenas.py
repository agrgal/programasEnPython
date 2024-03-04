# 4.7 String formatting pag. 43
cadena = "Mi nombre es {1} {0} y mi edad es {2}"
nombre ="Luis"
apellidos = "Pérez"
edad = 30
print(cadena.format(apellidos, nombre,edad))

cadena = "Mi nombre es {nombre} {apll1} y mi edad es {edad}"
print(cadena.format(nombre="Luis",apll1="Pérez",edad=30))