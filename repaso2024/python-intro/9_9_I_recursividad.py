 # generación de números primos por recursividad

def esPrimo(num, b=2):
    if num <= 2 or (num>2 and b>=num):
        # si el número es 2 ó 1, o b es mayor que el número, siendo éste mayor que 2
        # devuelve True
        return True
    elif num > 2 and b < num:  # mientras que no sea False, recursivamente calcula a
        # y siempre que sea False, ya se corta, pero... ¿Por qué? ¿¿??
        # print(num % b > 0, b)
        a = (num % b > 0) and esPrimo(num, b + 1)
        return a


for i in range(1,1001):
    es = "es primo" if esPrimo(i) else "es divisible entre uno anterior"
    print("El número {} {}".format(i,es))