# *-* coding: utf-8 *-*

import timeit

start = timeit.timeit()

numeros = []
for i in range(2, 10001):
    numeros.append(int(i))

# print numeros

primos = [2]

# print numeros[1] % primos[-1]

while len(numeros) > 1:
    # ultimo = primos[-1]
    print numeros[0]
    for x in numeros:
        # print numeros
        # print x
        # print ("Valor %s, ..., %s") % (x, x % ultimo)
        if (x % primos[-1] == 0):
            numeros.remove(x)
    primos.append(numeros[0])


# print numeros
# primos.insert(0,1)

print "\nTenemos %d números primos. Son: %s" % (len(primos), primos)

end = timeit.timeit()

print end - start