# -*- coding: utf-8 -*-

import numpy as np

def mostrar(a):
	print "\n",a
	print "Rango del array: ", a.ndim
	print "Tamaño del array en cada dimensión: ", a.shape
	print "Número total de elementos: ", a.size
	print "Tipos de elementos:", a.dtype.name
	print "Tamaño en bytes: ", a.itemsize
	print "Buffer: ", a.data

a = np.array([1,2,3])
mostrar(a)

a = np.array([[1,2,3], [4,2,4]], dtype=float)
mostrar(a)

a = np.array([[1,2,2.0], [4,0.2,4], [3,0.2,1.4]])
mostrar(a)

# a = np.array(1,2,3,4)  #¡Cuidado! No poner corchetes lanza un error
