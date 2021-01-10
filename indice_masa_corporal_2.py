# *-* coding: utf-8 *-*
miNombre = raw_input("Por favor, dime tu nombre: ")
miPeso = float(raw_input("Dime tu peso en kilogramos: "))
miAltura = float(raw_input("Dime tu altura en centímetros: "))

print "Tu nombre es %s, tu peso %.2f Kg y tu altura %.2f cm" % (miNombre, miPeso, miAltura)

miAltura = miAltura / 100  # para pasarla a metros

IMC = miPeso / (miAltura ** 2)

Escribe = "%s, tu índice de masa corporal es %.3f" % (miNombre, IMC)

# print Escribe

Escribe = "= " + Escribe + " ="

Recuadro = "=" * (len(Escribe) - 1)

print Recuadro + "\n" + Escribe + "\n" + Recuadro

# Cálculos del estado
misLimitesInferiores = [0, 18.5, 25, 30, 40, 1000]
misDefiniciones = ["delgadez", "un peso normal", "sobrepeso", "obesidad", "obesidad mórbida", "límite inalcanzable"]

indice = 0
for x in misLimitesInferiores:
    if (IMC < x):
        indice = misLimitesInferiores.index(x)
        #  print x, indice
        print "Presentas " + misDefiniciones[indice - 1]
        break

