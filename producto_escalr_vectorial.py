# *-* coding:utf-8 *-*

#  Define la función de entrada de datos al vector


def introduceVector(num):
    vector = []
    print ("\n")
    for i in range(0, 3):
        valor = float(input("Introduce coordenada " + chr(i + 120) + str(num) + ": "))
        vector.append(valor)
    print ("\n")
    return vector

#  Programa principal. Pide los datos
print ("Introduce el primer vector")
v1 = introduceVector(1)
print ("Introduce el segundo vector")
v2 = introduceVector(2)

# Cálculos: PRODUCTO ESCALAR
escalar = 0.0
# Recordar que es un float
for i in range(0, 3):
    escalar += v1[i] * v2[i]

print ("Producto escalar:  %.3f\n") % escalar

# Producto vectorial
fila0 = [1.0, -1.0, 1.0]
pv = []

for i in range(0, 3):
    signo = 1.0
    factor = 0.0
    for j in range(0, 3):
        for k in range(0, 3):
            signo = ((k > j) - (k < j)) * fila0[i] * (j != i) * (k != i)
            factor += v1[j] * v2[k] * signo
    # print(((" i: %d  --> %.3f y el signo: %f") % (i, factor, signo)))
    pv.append(factor)

print ("\nEl producto vectorial v1xv2 = [%.3f,%.3f,%.3f] ") % (pv[0], pv[1], pv[2])
