# -*- coding: utf-8 -*-

import doctest

def suma(x, y):
	""" Calcula la suma de dos números
    Argumentos: 
    x -- primer sumando 
    y -- segundo sumando 

	Test:
	>>> suma(23, 45)
	68
	
	>>> suma(24,-2)
	22
	"""
	return x + y
	
def resta(x, y):
	""" Calcula la resta de dos números
    
    Argumentos: 
    x -- minuendo 
    y -- sustraendo

	Test:
	>>> resta(23, 45)
	-22
	
	>>> resta(24,-2)
	26
	"""
	return x - y

if __name__ == "__main__": 
    doctest.testmod()
