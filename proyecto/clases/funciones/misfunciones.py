# -*- coding: utf-8 -*-


#  =========================
# Funciones
# =========================

	
# Devuelve lista con los factores descompuestos
def descomponer(num):
	lista = []
	if num<0:
		lista.append(-1)
		num = -1 * num
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
