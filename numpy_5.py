# -*- coding: utf-8 -*-

import numpy as np

def mifuncion(x,y):
	return 20*x-5*y

# matriz 3 x 4
a = np.fromfunction(mifuncion,(5,4),dtype=int)
print a

for row in a:
	print (row)

for element in a.flat:
	print (element)
