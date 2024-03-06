# mediante recursividad, indicar si un número es primo o no

def esprimo(num):
    if num==2:
        return True
    else:
        a = num % (num - 1)
        print (a)

print (esprimo(5))