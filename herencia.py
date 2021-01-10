# -*- coding: utf-8 -*-

class vehiculo(object):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80):
		self.color = c0
		self.combustible = comb0
		self.cilindrada = cil
		#capacidad del tanque de combustible
		self.tanque = tan
		self.maxTanque = tan
		return
		
	def andar(self):
		self.tanque -= 2
		return 

	def repostar(self):
		self.tanque = self.maxTanque
		return

class coche(vehiculo):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80, rued = 4):
		# llamo a la clase anterior vehiculo
		vehiculo.__init__(self,c0,comb0,cil,tan)
		# añado nueva característica
		self.ruedas = rued
		return
	
	def __str__(self):
		car = "Vehículo de " + str(self.ruedas) + " ruedas, " + self.combustible
		car += ", color " + self.color + " y cilindrada " + str(self.cilindrada)+"."
		car += "\nLe quedan en el tanque "+ str(self.tanque) + " litros."
		return car
	
class moto(vehiculo):
	
	def __init__(self, c0="rojo", comb0="diesel", cil=200, tan=80, rued = 2):
		# llamo a la clase anterior vehiculo
		vehiculo.__init__(self,c0,comb0,cil,tan)
		# añado nueva característica
		self.ruedas = rued
		return
	
	def __str__(self):
		car = "Vehículo de " + str(self.ruedas) + " ruedas, " + self.combustible
		car += ", color " + self.color + " y cilindrada " + str(self.cilindrada)+"."
		car += "\nLe quedan en el tanque "+ str(self.tanque) + " litros."
		return car
		

# =========================================
# Programa Principal
# =========================================

# crear dos vehículos distintos, con consideraciones iniciales
c1 = coche()
m1 = moto()

# Imprime información de los dos vehículos
print c1
print m1

# Crea un vehículo usando herencia para definir parte de sus caraterísticas
m2 = moto( "azul", "gasolina", 400, 200, 2)
# lo imprime
print m2

print "\n"

# Hago andar el vehículo 2, 10 veces.
for i in range(10):
	m2.andar()
print "He movido la moto 10 veces:\n", m2
# Le lleno el tanque
m2.repostar()
print "Le he llenado el tanque:\n", m2


	
