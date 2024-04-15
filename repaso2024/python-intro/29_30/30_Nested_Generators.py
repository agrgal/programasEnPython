# defino un generador para números pares

def pares(limite):
    valor = 0
    while valor < limite:
        yield valor
        valor += 2

for i in pares(8):
    for j in pares(8):
        print ("[{},{}]".format(i,j), end=", ")
    print()