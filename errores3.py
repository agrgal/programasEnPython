# *-* coding:utf-8 *-*

# Función F
def f():
	try:
		g()
	except ValueError, detalle:
		print "Caught a ValueError:", detalle.message

#Función G
def g(): 
	h()

# Función H
def h():
	raise ValueError('This is a test.')

# Programa principal
f()

