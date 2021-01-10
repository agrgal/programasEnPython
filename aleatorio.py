# -*- coding: utf-8 -*-

import random 
 
# Generar números aleatorios entre 49999 y 99999 
lista = [] 
 
for n in range(0, 50): 
    lista.append(random.randint(49999, 99999)) 
 
# Elegir un número al azar 
numero_al_azar = random.choice(lista) 
print numero_al_azar

# Elegir 5 números al azar 
numeros_al_azar = random.sample(lista, 5) 
print numeros_al_azar
 
# reordenar los elementos de una lista
mujeres = ["Ana", "Beatriz", "Camila", "Carmen", "Delia", "Dora", "Emilse"] 
random.shuffle(mujeres)

print mujeres
