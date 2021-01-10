# *-* coding:utf-8 *-*

#  Define la función de entrada de datos al vector


def introduceVector(num):
    vector = []
    for i in range(0, 3):
        valor = float(input("Introduce coordenada " + chr(i + 120) + str(num) + ": "))
        vector.append(valor)
    return vector


def introducePunto():
    punto = []
    for i in range(0, 3):
        valor = float(input("Introduce coordenada del punto A" + chr(i + 120) + ": "))
        punto.append(valor)
    return punto


def productoVectorial(u, v):
    # Producto vectorial
    fila0 = [1.0, -1.0, 1.0]
    pv = []
    for i in range(0, 3):
        signo = 1.0
        factor = 0.0
        for j in range(0, 3):
            for k in range(0, 3):
                signo = ((k > j) - (k < j)) * fila0[i] * (j != i) * (k != i)
                factor += u[j] * v[k] * signo
        # print(((" i: %d  --> %.3f y el signo: %f") % (i, factor, signo)))
        pv.append(factor)
    return pv


def productoEscalar(u, v):
    # Cálculos: PRODUCTO ESCALAR
    escalar = 0.0
    # Recordar que es un float
    for i in range(0, 3):
        escalar += u[i] * v[i]
    return escalar


def modulo(u):
    # Cálculos: Módulo de un vector
    mod = 0.0
    mod = productoEscalar(u, u) ** (0.5)
    return mod

#  Programa principal. Pide los datos
print "Cálculo del plano que tiene como vectores directores v1 y v2, y pasa por un punto"
print "=================================================================================\n"
print ("Introduce el primer vector")
v1 = introduceVector(1)
print ("Su módulo es |u| = %.3f\n") % (modulo(v1))
print ("Introduce el segundo vector")
v2 = introduceVector(2)
print ("Su módulo es |v| = %.3f\n") % (modulo(v2))
print ("Introduce el punto por donde pasa el plano")
OA = introducePunto()
print ("\n")

print ("Producto escalar v1v2:  %.3f\n") % (productoEscalar(v1, v2))

pVec = productoVectorial(v1, v2)
print ("El producto vectorial v1xv2 = [%.3f,%.3f,%.3f] ") % (pVec[0], pVec[1], pVec[2])

normal = [0.0, 0.0, 0.0]
for i in range(0, 3):
    normal[i] = pVec[i] / (modulo(v1) * modulo(v2))

# normal = productoVectorial(v1, v2) / (modulo(v1) * modulo(v2))
print ("El vector normal unitario N = v1xv2/(|v1||v2|) = [%.3f,%.3f,%.3f] ") % (normal[0], normal[1], normal[2])

# Ecuacion del plano; SI N = (A, B, C) y OA = (x1, y1, z1)
# Ax1 + By1 + Cz1 + D = 0, entonces D = - Ax1 -By1 - Cz1
# La determinción normal del plano es Ax+By+Cz+D=0

# calculo los coeficientes A, B, C, D de la ecuacion
coef = []
D = 0.0
for i in range(0, 3):
    D -= normal[i] * OA[i]
    coef.append(normal[i])
coef.append(D)

# Presentación de los coeficientes
NM = raw_input("Introduce [N] para normalizar, y otra tecla para no hacerlo. Pulsa intro: ")
if NM == "N" or NM == "n":
    dividir = 0.0
    for i in range(0, 4):
        if coef[i] != 0:
            dividir = coef[i]
            break
    for i in range(0, 4):
        coef[i] = coef[i] / dividir


# Muestro los coeficientes
cadena = ""
cadSigno = ""
for i in range(0, 3):
    if coef[i] < 0:
        cadSigno = "-"
    elif (coef[i] == 0 and i == 3):
        cadSigno = ""
    else:
        cadSigno = "+"
    if coef[i] != 0 and abs(coef[i]) != 1:
        cadena += cadSigno + "%.3f" % (abs(coef[i])) + chr(120 + i)
    elif abs(coef[i]) == 1:
        cadena += cadSigno + chr(120 + i)

if coef[3] < 0:
    cadena += "%.3f" % (coef[3])
elif coef[3] > 0:
    cadena += "+" + "%.3f" % (abs(coef[3]))

# Quitar el primer caracter de la cadena si es un más
if cadena[0] == "+":
    cadena = cadena[1:]

print("\nEcuación del plano %s = 0") % (cadena)







