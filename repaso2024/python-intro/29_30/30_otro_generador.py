# defino un generador para números pares

def pares(limite):
    valor = 0
    while valor < limite:
        yield valor
        valor += 2

print('Start')
for i in pares(200):
    print(i, end=', ')
print("Acabo")