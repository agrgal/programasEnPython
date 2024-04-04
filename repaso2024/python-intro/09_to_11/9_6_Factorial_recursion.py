# cálculo del factorial mediante recursividad

def factorial(n, depth=1):
    if n==1:
        print("\t"*depth,"Retorno 1")
        res = 1
    else:
        print('\t' * depth, 'Llamando al factorial recursivo(', n-1, ')')
        res = n*factorial(n-1,depth+1)
        print('\t' * depth, 'Devolviendo:', res)
    return res

def tail_factorial(n,accumulator=1):
    if n==0:
        return accumulator
    else:
        return tail_factorial(n-1,accumulator*n)

num = int(input("Dime un número entero positivo: "))
print (factorial(num))
print(tail_factorial(num))