 # generación de números primos por recursividad

def esPrimo(num, b=2):
    if num <= 2 or (num>2 and b>=num):
        return True
    elif num > 2 and b < num:  # mientras
        # print(num % b > 0, b)
        a = (num % b > 0) and esPrimo(num, b + 1)
        return a


for i in range(1,1001):
    es = "es primo" if esPrimo(i) else "es divisible entre otro anterior"
    print("El número {} {}".format(i,es))