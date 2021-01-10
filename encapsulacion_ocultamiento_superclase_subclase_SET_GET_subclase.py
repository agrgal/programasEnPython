# coding: utf-8 

# --------------------------------------------------------------------------
# SUPERCLASE o CLASE PADRE PUNTO
# Defino la superclase 
# Defino variables y métodos ocultos '__' precedidas de dos guiones bajos
# --------------------------------------------------------------------------
class Punto(): # Entre paréntesis se puede poner object class Punto(object):
	
	def __init__(self):
		self.__x=0.0 # Defino sus coordenadas como ocultas, y en principio como valores fijos
		self.__y=0.0 # de x=0 e y=0 (tipo float)
		
	def __str__(self):
		return "["+str(self.__x)+","+str(self.__y)+"]"
	
	def __add__(self,otro):
		suma = Punto()
		suma.__x = self.__x + otro.__x
		suma.__y = self.__y + otro.__y
		return suma
		
	def setPunto(self,x,y):
		# ¡Ojo! no comprueba si es un número
		self.__x = x
		self.__y = y

# --------------------------------------------------------------------------
# subclase, o clase que hereda las propiedades del "padre" o la "superclase"
# --------------------------------------------------------------------------
class Linea(Punto):
	
	def __init__(self,x1=0.0,y1=0.0,x2=0.0,y2=0.0):
		Punto.__init__(self) #inicializo la otra 
		self.P1 = Punto()
		self.P1.setPunto(x1,y1)
		self.P2 = Punto()
		self.P2.setPunto(x2,y2)
		self.__pendiente = (y2-y1)/(x2-x1) #ojo, no comprueba que x2-x1 <> 0 
		self.__ordenada = y1 - self.__pendiente * x1 

	def __str__(self):
		# NOTA: hay que obtener la impresión del punto a través de la función str si accedo a los objetos puntos
		# return str(self.P1)+"-"+str(self.P2)
		return "y="+str(self.__pendiente)+"x + "+str(self.__ordenada)

# programa principal

L1 = Linea(1,1,2,13.1) # definida por sus puntos

print L1
