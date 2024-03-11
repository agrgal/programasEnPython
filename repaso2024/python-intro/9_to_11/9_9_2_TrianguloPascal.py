def calcularcoeficiente(f,c):
    """
    :param f: int que representa la fila
    :param c: int que representa la columna
    :return: de forma recursiva, el valor del coeficiente en la posición fila, columna
    Si la columna es cero o coincide con el número de fila , devuelve 1.
    Si no, se calcula sumando el coeficiente en la fila anterior y la columna anterior
    más el coeficiente de la fila anterior y misma posición
            0   1   2   3   4...
    fila=0  1
    fila=1  1   1
    fila=2  1   2   1
    fila=3  1   3   3   1
    fila=4  1   4   6   4   1
    """
    if c==0 or c==f:
        return 1
    else:
        return calcularcoeficiente(f-1,c-1)+calcularcoeficiente(f-1,c)

def calcularFila(fila):
    """
    :param fila: número de la fila
    :return: una cadena centrada con los valores del triángulo de Pascal hasta dicha fila, y separado, el
    valor de la suma de todos los valores
     El bucle "i" calcula la suma y los coeficientes de una fila
     El bucle "j" construye las filas desde la cero a la "fila" dada
    """
    for j in range(0,fila+1):
        cadena=""
        suma= 0
        for i in range(0,j+1):
            suma = suma + calcularcoeficiente(j,i)
            cadena = cadena + str(calcularcoeficiente(j,i)) + " "

        print("{:^80}={:<10}".format(cadena,suma))


print(calcularcoeficiente.__doc__)
print(calcularFila.__doc__)
calcularFila(15) #Calcula el triángulo de Pascal hasta la fila 15.