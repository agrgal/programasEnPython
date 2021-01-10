# *-* coding: utf-8 *-*


def obtener():
    DNI = raw_input("Dame tu número de DNI: ")
    Nombre = raw_input("Nombre y apellidos: ")
    Telefono = raw_input("Dame tu número de teléfono: ")
    print ("\n")
    registro = [DNI, Nombre, Telefono]
    return registro

# Programa principal
agenda = {}

for i in range(3):
    registro = obtener()
    agenda[registro[0]] = registro[1:]

print agenda

bandera = 1
while bandera !=0:
    valor = raw_input("¿Qué número de DNI buscas? ")
    if agenda.has_key(valor):
        print ("Tu nombre es %s y tu número de teléfono %s") % (agenda[valor][0], agenda[valor][1])
    else:
        print("Lo siento, no la tengo en la agenda")
    bandera = raw_input("Introduce 0 para salir del programa agenda: ")
    bandera = int(bandera)


