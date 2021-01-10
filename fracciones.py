# -*- coding: utf-8 -*-

# =========================
# Funciones
# =========================

def introducir():
	t = 5
	while t>0: 
		try:
			print ("Tienes %d oportunidades de introducir un dato correcto: ") % (t)
			numerador = int(raw_input("Introduce numerador: "))
			denominador = int(raw_input("Introduce numerador: "))
			a = fraccion(numerador, denominador)
			return a
		except ZeroDivisionError:
			print ("El denominador no puede ser cero\n")
			t = t - 1
		except TypeError:
			print ("No has introducido un tipo correcto. Debe ser entero\n")
			t = t - 1
		except ValueError:
			print ("No has introducido un valor entero\n")
			t = t - 1
		except Exception, ex:
			print ("Error producido :") + str(ex)
			raise
	raise ValueError, "Has tenido cinco oportunidades de introducir un dato correcto"
	
# Devuelve lista con los factores descompuestos
def descomponer(num):
	lista = []
	pivote = 2
	while pivote<num:
		if num % pivote != 0:
			pivote = pivote + 1
		else:
			#introduce el pivote en la lista
			lista.append(pivote)
			#divide num entre el pivote
			num = num / pivote
			# print num, pivote
	#Cuando acaba introduce el número
	lista.append(num)
	return lista

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
		listanumerador = descomponer(self.numerador)
		listadenominador = descomponer(self.denominador)
		# bucle que empieza a reducir		
		listaIntermedia = []
		for i in listanumerador:
			if i in listadenominador:
				listadenominador.remove(i)
				listaIntermedia.append(i)
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
		return self + resta
		
	def inversa(self):
		a = fraccion(self.denominador,self.numerador)
		a.reducir
		return a
		
	def __div__(self, otra):
		dividir = otra.inversa()
		return self * dividir
		
# =========================
# Programa principal
# =========================


print "Introduce fracción primera: "
f1 = introducir()
print "primera fracción:", f1, "\n"

print "Introduce fracción segunda: "
f2 = introducir()
print "segunda fracción:", f2, "\n"
		
f1.reducir()
print "primera fracción reducida:", f1, "\n"
f2.reducir()
print "segunda fracción reducida:", f2, "\n"

print "Inversa 1ª fracción reducida:", f1.inversa(), "\n"
print "Inversa 2ª fracción reducida:", f2.inversa(), "\n"

print "Suma de las dos: ", f1 + f2, "\n"
print "Resta de las dos: ", f1 - f2, "\n"
print "Multiplicar las dos: ", f1 * f2, "\n"
print "Dividir las dos: ", f1 / f2, "\n"
