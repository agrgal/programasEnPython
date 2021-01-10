# -*- coding: utf-8 -*-
import random

imagen = open("prueba.bmp", "wb")

lista = []
for i in range(1000):
    lista.append(random.randrange(0,256))
    imagen.write(str(lista[i]))

print lista

imagen.close()