# -*- coding: utf-8 -*-

import funciones.misfunciones as fun 

# =========================
# Clases
# =========================

class fraccion(object):
	
	def __init__(self, x0 = 1, y0 = 1):
		try: 			
			self.numerador = x0
			self.denominador = y0
			test = x0 / y0
			return 
		except ZeroDivisionError:
			raise 
		
	def __str__(self):
		if self.denominador >1:
			return str(self.numerador) + "/" + str(self.denominador)
		elif self.denominador == 1:
			return str(self.numerador)
		else:
			return "No es posible representar"
		
	def reducir(self):
		# Obtiene componentes
		listanumerador = fun.descomponer(self.numerador)
		listadenominador = fun.descomponer(self.denominador)
		# bucle que empieza a reducir		
		listaIntermedia = []
		for i in listanumerador:
			if i in listadenominador:
				listadenominador.remove(i)
				listaIntermedia.append(i)
		# print "Numerador: ",listanumerador
		# print "Intermedia: ",listaIntermedia
		# print "Denominador: ",listanumerador
		for i in listaIntermedia:
			listanumerador.remove(i)
		# convierte la fracción a la reducida
		self.numerador = 1
		for i in listanumerador:
			self.numerador *= i
		self.denominador = 1
		for i in listadenominador:
			self.denominador *= i
		# print listanumerador, listadenominador, listaIntermedia
		return 
		
	def __add__(self, otra):
		numerador = self.numerador*otra.denominador + self.denominador*otra.numerador
		denominador = self.denominador * otra.denominador
		suma = fraccion(numerador, denominador)
		suma.reducir()
		return suma
		
	def __mul__(self, otra):
		numerador = self.numerador * otra.numerador
		denominador = self.denominador * otra.denominador
		multiplicar = fraccion(numerador, denominador)
		multiplicar.reducir()
		return multiplicar
		
	def __sub__(self,otra):
		resta = fraccion(1,1)
		resta.numerador = -1 * otra.numerador
		resta.denominador = otra.denominador
		restar = self + resta
		restar.reducir()
		return restar
		
	def inversa(self):
		a = fraccion(self.denominador,self.numerador)
		a.reducir()
		return a
		
	def __div__(self, otra):
		dividir = otra.inversa()
		division = self * dividir
		division.reducir()
		return division
