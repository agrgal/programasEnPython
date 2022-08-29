def mcd(n1,n2): # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
	minimo = min(n1,n2)
	n = 0
	for i in range(1,minimo):
		if n1%i==0 and n2%i==0:
			n=i
	return n

print(mcd(10,15))
print(mcd(15,10))

print (mcd(20,30))
print (mcd(100,125))
