def calcularcoeficiente(f,c):
    if c==0 or c==f:
        return 1
    else:
        return calcularcoeficiente(f-1,c-1)+calcularcoeficiente(f-1,c)

def calcularFila(fila):
    for j in range(0,fila+1):
        cadena=""
        suma= 0
        for i in range(0,j+1):
            suma = suma + calcularcoeficiente(j,i)
            cadena = cadena + str(calcularcoeficiente(j,i)) + " "

        print("{:^80}={:<10}".format(cadena,suma))


calcularFila(15)