# Vamos a jugar a los dados
import random

seguir='s'

while seguir=='s':
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    print ("Dado 1 {dado1} y Dado 2 {dado2}".format(dado1=dice1,dado2=dice2))
    print()
    seguir = input("¿Quieres seguir jugando? [s/n]:")