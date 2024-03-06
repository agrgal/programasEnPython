# programa de los números aleatorios.
# Debo encontrar un número aleatorio antes de 4 jugadas

import random

num = random.randint(1,10)
contarJugadas = 1

print("Juego de la adivinanza")
guess = int(input("Adivina un número entre el 1 y el 10: "))

while num!=guess:
    if contarJugadas < 4:
        if num>guess:
            print("Lo siento, el número es mayor que el que has jugado")
        else:
            print("Lo siento, el número es menor que el que has jugado")
        guess = int(input("Inténtalo otra vez: "))
        contarJugadas+=1
        continue
    break

if num==guess:
    print("Enhorabuena. Acertaste el número jugado, el {num}, en {tiradas} tiradas".format(num=num,tiradas=contarJugadas))
else:
    print("Lo siento. No has completado el juego. El número era el {num}".format(num=num))