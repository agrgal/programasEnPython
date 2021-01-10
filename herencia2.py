# -*- coding: utf-8 -*-

class vehiculo(object):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80, mt=("",0)):
		self.color = c0
		self.combustible = comb0
		self.cilindrada = cil
		#capacidad del tanque de combustible
		self.tanque = tan
		self.maxTanque = tan
		self.motor = mt
		return
		
	def andar(self):
		self.tanque -= 2
		return 

	def repostar(self):
		self.tanque = self.maxTanque
		return
		
class motor(object):
	def __init__(self, marca="Mercedes", cilindros=4):
		self.marca = marca
		self.cilindros = cilindros
		return
		
	def __str__(self):
		return "["+self.marca + ":" + str(self.cilindros)+ "]"
		
	def gripar(self):
		self.marca="Estropeado"
		self.cilindros=0
		return

class coche(vehiculo):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80, rued = 4, mt=("",0) ):
		# llamo a la clase anterior vehiculo
		vehiculo.__init__(self,c0,comb0,cil,tan, mt)
		# añado nueva característica
		self.ruedas = rued
		return
	
	def __str__(self):
		car = "Vehículo de " + str(self.ruedas) + " ruedas, " + self.combustible
		car += ", color " + self.color + " y cilindrada " + str(self.cilindrada)+"."
		car += "\nDe motor: " + str(self.motor) + "."
		car += "\nLe quedan en el tanque "+ str(self.tanque) + " litros."
		return car
	
class moto(vehiculo):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80, rued = 2, mt=("",0) ):
		# llamo a la clase anterior vehiculo
		vehiculo.__init__(self,c0,comb0,cil,tan,mt)
		# añado nueva característica
		self.ruedas = rued
		return
	
	def __str__(self):
		car = "Vehículo de " + str(self.ruedas) + " ruedas, " + self.combustible
		car += ", color " + self.color + " y cilindrada " + str(self.cilindrada)+"."
		car += "\nDe motor: " + str(self.motor) + "."
		car += "\nLe quedan en el tanque "+ str(self.tanque) + " litros."
		return car
		

# =========================================
# Programa Principal
# =========================================

# Dos motores
mt1 = motor("RENAULT",12)
mt2 = motor("HONDA",6)

# crear dos vehículos distintos, con consideraciones iniciales
c1 = coche("negro","gasolina",500,120,4,mt1)
m1 = moto("amarilla","diesel",900,180,2,mt2)

# Imprime información de los dos vehículos
print c1
print m1

# Crea un vehículo usando herencia para definir parte de sus caraterísticas
m2 = moto( "azul", "gasolina", 400, 200, 2,mt2)
# lo imprime
print m2

print "\n"

# Hago andar el vehículo 2, 10 veces.
for i in range(10):
	m2.andar()
print "He movido la moto 10 veces:\n", m2, "\n"
# Le lleno el tanque
m2.repostar()
print "Le he llenado el tanque:\n", m2, "\n"

# Gripo el motor de la segunda moto
m2.motor.gripar()
print "¿Qué le ha pasado al motor de la moto?: ",m2.motor


	
