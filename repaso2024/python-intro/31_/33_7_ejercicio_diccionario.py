# Diccionario para hacer una caché

from timeit import default_timer

def timer(func):
    def inner(valor):
        tcero = default_timer()
        mm = func(valor)
        tfin=default_timer()
        print("Llamada a la función {} con valor {}\n y resultado {}\n tarda {}s"
              .format(func.__name__,valor,mm,tfin-tcero))
    return inner
@timer
def factorial(n):
    global cache
    if n == 1:
        return 1
    else:
        if str(n) in cache:
            return cache[str(n)]
        valor = 1
        for i in range(1,n+1):
            valor = valor * i
        cache[str(n)] = valor
        return valor

cache={} #diccionario donde se añaden los valores, en principio nulo
factorial(5)
factorial(10)
factorial(100)
factorial(1000)
# La segunda que vez que lo llama tarda mucho menos, porque está almacenado en la caché
factorial(5)
factorial(10)
factorial(100)
factorial(1000)

print(cache)



