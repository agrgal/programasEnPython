# programa que usa un generador para generar los números primos

def primos(limite):
    j = 2
    milista = [] # No sé si esto es correcto, porque voy almacenando números... ¿¿??
                 # pero si no, ¿como lo hago?
    while j < limite:
        # print(milista)
        for n in milista:
            if j % n == 0:  # si el elemento j es múltiplo de los de la lista se rompe el bucle
                break
        else:  # solo se ejecuta si se acaba el for
            yield j
            milista.append(j)
        j += 1


for k in primos(90):
    print("El número {} es primo".format(k))



