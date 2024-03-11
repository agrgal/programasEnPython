# Programa CALCULADORA
# ====================

#  Functions
def presentacion():
    print("Bienvenidos al programa calculadora")


def add(x, y):
    """ Add two numbers"""
    return x + y


def subtract(x, y):
    """ Subtract two numbers"""
    return x - y


def mult(x, y):
    """ Multiply two numbers """
    return x * y


def divide(x, y):
    """ Divide two numbers """
    return x / y


def get_number(tipo="first"):
    """ Devuelve un número introducido desde la consola"""
    return int(input("Give me the {} number: ".format(tipo)))


def print_result(a, b, op, resultado):
    print("La operación {} sobre los números {} y {} es {}".format(op, a, b, resultado))


#  =================================================

#  Main program
presentacion()

while True:
    operator = input("Dime la operación [+ , - , x ,  /]: ")
    n1 = get_number("first")
    n2 = get_number("second")

    if operator == "+":
        print_result(a=n1, b=n2, op=operator, resultado=add(n1, n2))
    elif operator == "-":
        print_result(a=n1, b=n2, op=operator, resultado=subtract(n1, n2))
    elif operator == "x":
        print_result(a=n1, b=n2, op=operator, resultado=mult(n1, n2))
    elif operator == "/":
        print_result(a=n1, b=n2, op=operator, resultado=divide(n1, n2))

    fin = input("Terminar [s/n]: ")
    if fin == "s":
        break
#  =================================================
