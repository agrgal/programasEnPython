# -*- coding: utf-8 -*-

import numpy as np

def mifuncion(x,y):
	return 20*x-5*y

# matriz 3 x 4
a = np.fromfunction(mifuncion,(5,4),dtype=int)
print a

# Indexado de un eje o fila
print "En la posición 2 (3ª): ",a[2]
# Indexado de varias filas
print "De la 2 a la 4: ", a[2:5]
# Un sólo elemento
print "Elemento 2,3: ", a[2,3]
# lo que vale en cada fila la columna 2. Probar también a[:,1]
print "Columna nº 2: ", a[0:5,1]
print "Tres elementos de la 2ª fila: ",a[1,0:3]
print "Cada eje desde 2l 2º al 3º",a[1:3, : ]
print "La última fila: ",a[-1]
print "La penúltima fila: ",a[-2]
# otras formas de representar
print "Filas de la 3ª en adelante: ",a[2,...]
print "Filas hasta la 3ª: ", a[...,3]

