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


def get_number(tipo="primer"):
    """ Devuelve un número introducido desde la consola.
        Comprueba si es un valor numérico o no, y si no lo es repite hasta que lo sea"""
    nn = ""
    while not nn.isnumeric():
        nn = input("Dame el {} número: ".format(tipo))
        if not nn.isnumeric():
            print("Introduce un valor numérico.")
        else:
            return int(nn)  # Debe pasarlos a números


def print_result(a, b, op, resultado):
    """ Devuelve el resultado """
    print("La operación {} sobre los números {} y {} es {}".format(op, a, b, resultado))


def elige_op():
    """ Esta función permite elegir e imprimir un tipo de operación"""
    op = 0
    while not 1 <= op <= 4:
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Dividir")
        op = int(input("Elige una operación: "))
        if not 1 <= op <= 4:
            print("operación incorrecta; vuelve a elegir")
    return op   # Devuelve el código de la operacion

#  =================================================

# =============
#  Main program
# =============


presentacion()
while True:
    operator = elige_op()
    n1 = get_number("primer")
    n2 = get_number("segundo")
    if operator == 1:
        print_result(a=n1, b=n2, op=operator, resultado=add(n1, n2))
    elif operator == 2:
        print_result(a=n1, b=n2, op=operator, resultado=subtract(n1, n2))
    elif operator == 3:
        print_result(a=n1, b=n2, op=operator, resultado=mult(n1, n2))
    elif operator == 4:
        print_result(a=n1, b=n2, op=operator, resultado=divide(n1, n2))
    fin = input("Terminar [s/n]: ")
    if fin == "s":
        break
print("Hasta luego, nos vemos!!!!")
#  =================================================
