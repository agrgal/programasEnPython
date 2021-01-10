# *-* coding:utf-8 *-*


# Funciones

def introduce(m):
    A = []
    for i in range(m):
        A.append([0] * m)
    for i in range(m):
        for j in range(m):
            cadena = "Dime el índice %d,%d: " % (i, j)
            A[i][j] = float(raw_input(cadena))
    for i in range(m):
        print ("| %s |") % (A[i])
    return A


def determinante(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]

# Programa principal
rango = int(raw_input("¿Qué rango tiene?"))

B = introduce(rango)
# determinante
det = determinante(B)
print ("Determinante = %f") % (det)
