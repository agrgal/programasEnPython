def color_frecuente(lista):
	prioridad=['azul', 'rojo', 'verde', 'amarillo']
	paraContar=[]
	for i in prioridad:
		contar=0
		for j in lista:
			if (j==i):
				contar=contar+1
		paraContar.append([contar,i])
	paraContar.sort() # los ordena de menor a mayor
	paraContar=paraContar[::-1] # orden inverso
	valorMaximo=paraContar[0][0] #Saco el máximo de todos ellos
	colorMaximo=[]
	for i in prioridad:
		# print(i)
		for n in paraContar:	
			# print (n)		
			if n[0]==valorMaximo and n[1]==i and len(colorMaximo)<=0:
				colorMaximo=n[::-1] # en orden inverso
				break	
	return str(colorMaximo) # El elemento 0 pero invertido

# colores=['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo','verde', 'verde', 'azul', 'amarillo', 'azul', 'azul','verde', 'verde', 'verde', 'amarillo', 'amarillo']
# colores = ['rojo', 'rojo', 'azul', 'azul']
# colores = ['verde', 'verde', 'amarillo', 'amarillo']
colores = ['verde','azul', 'rojo','verde', 'amarillo','azul', 'amarillo','amarillo','rojo']
print(color_frecuente(colores))	
