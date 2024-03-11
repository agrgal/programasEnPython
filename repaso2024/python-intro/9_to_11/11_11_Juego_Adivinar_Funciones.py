# Juego de adivinar un número con funciones
import random


# Funciones
def generar_aleatorio(minN=2, maxN=10):
    return random.randint(minN, maxN)


def comprobar_num(valor2, multiplicar=4):
    if valor2 > multiplicar:
        return "El valor es mayor que el que tienes que adivinar", 1
    elif valor2 < multiplicar:
        return "El valor es menor que el que tienes que adivinar", -1
    else:
        return "Acertaste. El número era {}".format(valor2), 0


def check_valido(numero):
    return 4 <= numero <= 100


# Pantalla principal
# Se trata de adivinar la multiplicación de dos números
print("Bienvenido al juego")
n1 = generar_aleatorio()
n2 = generar_aleatorio()
mult = lambda x, y: x * y  # Función anónima, que permite calcular... LA MULTIPLICACIÓN... Orrr
nn = mult(n1, n2)

tiradas = 0
while tiradas < 10:
    guess = -1
    while not check_valido(guess):
        guess = int(input("Tirada {}: Introduce un número del 4 al 100: ".format(tiradas + 1)))
    cadena, valor = comprobar_num(valor2=guess, multiplicar=nn)
    print("Tirada: {} >> {}".format(tiradas + 1, cadena))
    if valor == 0:
        break
    tiradas += 1
else:
    print("Me temo que has perdido todas tus tiradas")

print("Juego terminado")
