# *-* coding:utf-8 *-*

# Función Raíz Cuadrada
def raizCuadrada(n):
	# pre: el número n debe ser un número mayor que cero
	# post: se devuelve el valor de la raíz
	assert n>=0, "Tu número es negativo"
	raiz = n ** (0.5)
	return raiz
	
print raizCuadrada(-35)
	



