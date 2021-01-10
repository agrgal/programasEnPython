# *-* coding:utf-8 *-*

A = []

for i in range(2):
    A.append([0]*2)

for i in range(2):
    for j in range(2):
        cadena = "Dime el índice %d,%d: " % (i, j)
        A[i][j] = float(raw_input(cadena))

for i in range(2):
    print ("| %s |") % (A[i])

# determinante
det = 0.0
for i in range(2):
    for j in range(2):
        if (j != i):
            signo = (-1) * (i<j)+(i>j)*(1)
            det += A[i][j]*A[j][i]
            print i,j,A[i][j],A[j][i], det

print ("Determinante = %f") % (det)
