# -*- coding: utf-8 -*-

import numpy as np

# matriz 3 x 4
a = np.arange(12).reshape(3,4)
print a, a.shape

#operaciones unitarias, elemento a elemento
print "Suma de todos los elementos: ",a.sum()
print "Mínimo de todos los elementos: ",a.min()
print "Máximo de todos los elementos: ",a.max()
print "Suma por cada columna: ",a.sum(axis=0)
# axis = 0 ==>  columnas, axis =1 ==> filas
print "Mínimo de cada fila: ",a.min(axis=1)
print "Suma acumulativa por filas: ", a.cumsum(axis=1)
# Funciones
print "Exponencial a cada número: ",np.exp(a)
print "Raíz cuadrada a cada número: ",np.sqrt(a)



