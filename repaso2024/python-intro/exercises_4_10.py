
valores = 'Denyse,Marie,Smith,21,London,UK'
print(valores.replace(","," "))

nombre = input("Give me your name: ")
apellido = input ("Give me your family name: ")
nombreCompleto = nombre+ " " + apellido

print(nombreCompleto)
print("La longitud de tu nombre es {}".format(len(nombreCompleto)))
nombreCompleto= nombreCompleto.upper()
print("Tu nombre en mayúsculas es {}".format(nombreCompleto))
busqueda = 'Albus'
print("¿Contiene tu nombre {}? {}".format(busqueda, (nombreCompleto.find(busqueda)>0)))
