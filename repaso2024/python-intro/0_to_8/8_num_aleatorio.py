# programa de los números aleatorios.
# Debo encontrar un número aleatorio antes de 4 jugadas

import random

print("Juego de la adivinanza")

again="s"
while again=="s":

    num = random.randint(1, 10)
    contarJugadas = 1
    guess = int(input("Adivina un número entre el 1 y el 10: "))

    while num!=guess:
        if guess==-1: #cheat mode
            print("Bueeeeenooo... el número que tienes que adivinar es el {a} ".format(a=num))
        if abs(num-guess)==1:
            print("¡¡Uy!! Casi... Estas cerca")
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

    again=input("¿Quieres jugar otra vez? [s/n]: ")

print("Game over")
