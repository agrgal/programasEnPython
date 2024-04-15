# defino un generador para números pares

def pares(limite):
    valor = 0
    while valor < limite:
        yield valor
        valor += 2

mispares = pares(80)
print(next(mispares))
print(next(mispares))
print(next(mispares))
