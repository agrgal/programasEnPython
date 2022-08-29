def promedio_std(lista):
	x = sum(lista)/len(lista)
	suma=0
	for i in lista:
		suma=suma+(i-x)**2
	y=(suma/len(lista))**(0.5)
	return (x,y)

lista=[]
numeros=""
for i in range(1,101):
	numeros=numeros+str(i)+","
	lista.append(i)
# print(lista)
print(numeros)
print(promedio_std(lista))
	
