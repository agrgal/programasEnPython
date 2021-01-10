# -*- coding: utf-8 -*-

# ===================================================
# Funciones
# ===================================================

def listado(nodo):
	
	while nodo:
		print nodo
		nodo = nodo.prox

# ===================================================
# Clases
# ===================================================


class nodo(object):
	
	def __init__(self, valor = None, proximo = None):		
		self.valor = valor
		self.prox = proximo
		return
		
	def __str__(self):
		return "["+str(self.valor)+"]"
		
# ===================================================
# Programa principal
# ===================================================

v1 = nodo("Plátano")
v2 = nodo("Manzana",v1)
v3 = nodo("Fresa",v2)

print v1, v2, v3

print listado(v2)
		


	
