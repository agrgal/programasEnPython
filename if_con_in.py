# *-* coding: utf-8 *-*
miNombre = raw_input("Escribe tu nombre: ")
misNombres = ["JUAN", "JAIME", "ANA", "FRANCISCO", "MARÍA", "LUISA", "CARMEN", "ANTONIO"]

"""Para igualar, paso miNombre a mayúsculas. Así comparo mejor"""
miNombre = miNombre.upper()

if miNombre in misNombres:
    print "Está en la lista"
else:
    print "¡Oh! No está en la lista"
