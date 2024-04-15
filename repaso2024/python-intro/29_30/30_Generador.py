# Uso de generadores. Necesaria una función o módulo.

def generador(n):
    for i in range(n):
        if i%2 == 0:
            yield i

for k in generador(20):
    print (k)