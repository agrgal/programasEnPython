# *-* coding: utf-8 *-*
miEdad = int(raw_input("¿Cuál es tu edad?: "))
"""¡Cuidado! Convertir la variable en numérica con int """

if miEdad < 18:
    print "¡Aún no soy mayor de edad! :-("
elif ((miEdad >= 18) and (miEdad < 65)):
    print "¡Eres mayor de edad y tienes edad de trabajar! :-)"
else:
    print "¡Ya tienes edad de jubilarte! :-)"