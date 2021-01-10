# *-* coding:utf-8 *-*


# Funciones


def introduce(m):
    # define la matriz A
    A = []
    # por cada valor hasta el rango
    for i in range(m):
        # Añade una fila de m ceros
        # La matriz de rango n x n se compone de n listas, cada una de n elementos
        A.append([0] * m)
    # Recorre los índices, e introduce
    for i in range(m):
        for j in range(m):
            cadena = "Dime el índice %d,%d: " % (i + 1, j + 1)
            A[i][j] = float(raw_input(cadena))
    imprime(A)
    return A


def imprime(A):
    print ("\n")
    for i in range(len(A)):
        print ("| %s |") % (A[i])
    print("\n")


"""
def determinante2(l):
    n=len(l)
    if (n>2):
        i=1
        t=0
        suma=0.0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m != t):
                        d[t1].append(l[t1][m])
                    m+=1
                t1+=1
            l1=[d[x] for x in d]
            suma = suma + i * l[0][t] * determinante2(l1)
            i=i*(-1)
            t+=1
        return suma
    else:
        return (l[0][0]*l[1][1]-l[0][1]*l[1][0]) """

def determinante(A):
    B = [k[:] for k in A]
    n = len(A)
    suma = 0.0
    if n > 2:
        # print("\nEntrada Matriz de rango %d") % (n)
        # imprime(B)
        for i in range(n):
            factor = B[0][i]
            signo = -2 * (i % 2) + 1
            B.remove(B[0])
            # imprime(B)
            for j in range(0, n - 1):
                # B[j][i] = -1000  B[j].remove(B[j][i])
                # No se puede poner remove pues QUITA EL PRIMER
                # elemento de la lista, no el que está en la posición
                # correcta. Para ello usar POP
                B[j].pop(i)
            # imprime(B)
            suma = suma + factor * signo * determinante(B)
            # if n > 3:
                # print ("Factor: %.3f ; signo: %d ; suma arrastrada: %.3f") % (factor, signo, suma)
                # imprime(B)
            B = [k[:] for k in A]
        return suma
    else:
        # print ("determinante orden 2: %.3f") % ((B[0][0] * B[1][1]) - (B[0][1] * B[1][0]))
        # imprime(B)
        return (B[0][0] * B[1][1]) - (B[0][1] * B[1][0])

# Programa principal
rango = int(raw_input("¿Qué rango tiene?: "))

C = introduce(rango)
# determinante
det=determinante(C)
print ("Determinante de la matriz = %f") % (det)
