# coding: utf-8 

import math as mt

# --------------------------------------------------------------------------
# SUPERCLASE o CLASE PADRE PUNTO
# Defino la superclase 
# Defino variables y métodos ocultos '__' precedidas de dos guiones bajos
# --------------------------------------------------------------------------
class Punto:
	
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
		# Una fórmula que indica un cuadrante, sin mucha complicación
		# si x>0 e y>0 --> 1, si x<0, y>0, 2, si x<0, y<0 -->4, y x > 0, y<0 --> -1
		self.__cuadrante = mt.copysign(1,self.x)*mt.copysign(1,self.y) + 3 * (self.x < 0)
		self.cuadrante2 = self.__cuadrante
		
	def __str__(self):
		return "["+str(self.x)+","+str(self.y)+"]"
	
	def __add__(self,otro):
		suma = Punto(0,0)
		suma.x = self.x + otro.x
		suma.y = self.y + otro.y
		return suma
		
	# Comenta, descomenta las siguientes dos líneas de definicioón del método... ¿Cuál funcionará?
	# def __obtenerCuadrante(self):
	def obtenerCuadrante(self):
		# Descomenta y comenta cada una de las dos líneas return... ¿Cuál funcionará?
		# return self.cuadrante2
		return self.__cuadrante

# programa principal

A = Punto(-3,-4)
B = Punto(2,5)
print A , B
print A + B

# Ninguna de las siguientes tres expresiones funcionarán porque no son accesibles
# están de forma privada. Si las ejecutamos, nos dará un error. Estas variables están ocultas
# print A.__cuadrante
# print A.cuadrante
print A.obtenerCuadrante()
print A.cuadrante2
