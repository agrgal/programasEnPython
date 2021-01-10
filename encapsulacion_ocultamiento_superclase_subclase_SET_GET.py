# coding: utf-8 

# --------------------------------------------------------------------------
# SUPERCLASE o CLASE PADRE PUNTO
# Defino la superclase 
# Defino variables y métodos ocultos '__' precedidas de dos guiones bajos
# --------------------------------------------------------------------------
class Punto:
	
	def __init__(self):
		self.__x=0 # Defino sus coordenadas como ocultas, y en principio como valores fijos
		self.__y=0 # de x=0 e y=0
		
	def __str__(self):
		return "["+str(self.__x)+","+str(self.__y)+"]"
	
	def __add__(self,otro):
		suma = Punto()
		suma.__x = self.__x + otro.__x
		suma.__y = self.__y + otro.__y
		return suma
	
	# Establezco un método SET. Así accedo a variables ocultas
	# Acceder así a estas variables me permite tener cierto ocntrol sobre ellas.
	def setPunto(self,x,y):
		if (x<0 and y<0):
			print "No puedes establecer un punto del tercer cuadrante"
		else:
			self.__x = x
			self.__y = y
			print "Introducido correctamente un punto ",self
	
	def getPunto(self):
		print "Obtengo el punto... ",self


# programa principal

A = Punto()
B = Punto()

A.setPunto(3,2) # punto correcto, del primer cuadrante
B.setPunto(-1,4) # punto correcto, del 2º cuadrante
A.setPunto(-1,-2) # Punto incorrecto del tercer cuadrante

# Ejemplos del método GET
A.getPunto() # Ejemplos del método GET
B.getPunto()
C = A + B
C.getPunto()

# Romper el encapsulamiento
print A._Punto__x
