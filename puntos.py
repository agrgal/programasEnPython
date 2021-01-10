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
		dx = self.x+-otro.x
		dy = self.y+otro.y
		return punto(dx,dy)		
		
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
B = punto(2,3)

# Imprime los puntos
A.imprimir()
B.imprimir()

print A.distancia(B)

# resta de los dos puntos
# C = A.resta(B)
# ¡¡No puedo hacer C = A - B!!
C = A - B
print C
