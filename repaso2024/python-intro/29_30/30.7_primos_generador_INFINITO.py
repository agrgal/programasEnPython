# programa que usa un generador para generar los números primos

def es_primo(n):
    if n < 2:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


def primos(inicial):
    j = inicial
    while True:
        if es_primo(j):
            yield j
        j += 1


p = primos(0)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# Los siguientes 100 números
for k in range(0, 101):
    print("El primo nº {} es el {}".format(k, next(p)))
