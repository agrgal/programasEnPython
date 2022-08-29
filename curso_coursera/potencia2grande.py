def exponente(n): # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
	from math import log
	return int(log(n)//log(2))


print(exponente(63))
