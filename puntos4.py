# *-* coding:utf-8 *-*

# ======================================================
# FUNCIONES
# ======================================================
# Validaciones
def es_numero(num):
	# indica si es o no un valor numérico
	return isinstance (num, (int, float, complex, long))

# ======================================================
# CLASES
# ======================================================
# clase puntos
class punto(object):
	""" Clase que permite trabajar con puntos en el plano, 
	en coordenadas cartesianas, x e y"""
	
	def __init__(self, x0=0.0, y0=0.0):
		""" pre: los puntos deben definirse con sus coordenadas x
		e y - tipo float - y pueden establecerse en la llamada inicial.
		La notación superior x0=0.0 e y0=0.0 indica los valores iniciales
		si no se define en la llamada """
		if es_numero(x0) and es_numero(y0):
			self.x = x0
			self.y = y0
		else:
			raise TypeError("x e y deben ser números")
	
	def imprimir(self):
		print self		
		
	def __str__(self):
		""" Muestra el punto como un par ordenado. """
		return "[" + str(self.x) + ", " + str(self.y) + "]"

	def __sub__(self, otro):
		"""Devuelve un punto que es la resta de otros dos"""
		dx = self.x-otro.x
		dy = self.y-otro.y
		return punto(dx,dy)
		
	def __add__(self,otro):
		"""Suma las coordenadas de dos puntos"""
		return self - otro * (-1)
		
	def __mul__(self, factor):
		""" Multiplicar un número o factor por un vector o punto """
		dx = factor * self.x
		dy = factor * self.y
		return punto (dx,dy)	
		
	def __eq__(self,otro):
		""" Determina si dos puntos son iguales """
		return (self.x == otro.x and self.y == otro.y)
		
	def __ne__(self,otro):
		""" Si dos puntos son distintos """
		return not self == otro
		
	def ordenar_por_y(self, otro):
		""" Ordenamos por coordenada y """
		diferencia = self.y - otro.y
		if diferencia>1:
			return 1
		elif diferencia<1:
			return -1
		else:
			return 0
		
	def norma(self):
		"""Devuelve la norma de un vector"""
		return (self.x ** 2 + self.y ** 2) ** (0.5)
		
	def distancia(self, otro):
		"""Devuelve la distancia entre dos puntos """
		vectorResta = self - otro
		return vectorResta.norma()
	
		

# ======================================================
# Programa principal
# ======================================================
# Punto A, # Defino valores al principio
A = punto(6,7)

# Punto B. Sin definir valores al principio.
B = punto(4,3)

# Imprime los puntos
print ("A = %s") % (A)
print ("B = %s") % (B)

#Cinco veces A
print ("5 veces el punto A %s es %s") % (A, A * 5)
print ("La norma de A es %.2f") % (A.norma())
print ("La norma de B es %.2f") % (B.norma())

C = punto(2,4)
D = punto(100,0.5)

print "¿Son iguales (2,4) y A - B?" , C == A - B, A - B
print "¿Son iguales (2,4) y A + B?" , C == A + B, A + B

lista = [A, B, C,D ]
lista.sort(cmp=punto.ordenar_por_y)

for i in lista:
	print i
