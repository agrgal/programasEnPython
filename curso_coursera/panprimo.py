def panprimo(n): # escribe tu función aquí, recuerda seguir cuidadosamente
# las instrucciones respecto a argumentos y retorno
	devuelve=True
	primo = int(str(n)[-3:])
	i=2
	#1) comprueba si es primo
	while i<primo and devuelve==True:
		if primo%i!=0:
			i+=1
		else:
			devuelve=False
	#2) comprueba si es pandigital
	for i in range(0,10): #rango de 0 a 9
		if not (str(i) in str(n)):
			devuelve = False
			break
	#3) devolver
	return devuelve

print (panprimo(1234567890379)) #true
print (panprimo(1234567897379)) #No es pandigital FALSE
print (panprimo(1234567890111)) #No es primo FALSE
print (panprimo(1234567890199)) #No es primo FALSE
