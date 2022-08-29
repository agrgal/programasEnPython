'''
Programa que resuelve ecuaciones de tres variables por el método de Gauss 
No tiene en cuenta posibles errores. 
'''

# declaración de variables y listas
a=[[0,0,0,0],[0,0,0,0],[0,0,0,0]] # listas vacías
# pidiendo datos
for i in range(0,3):
	print("ecuación %d" % (i+1))
	print("===========")
	for j in range(0,3):
		a[i][j] = float(input("Dime el factor %s de la ecuación %d: " % (chr(j+1),i+1)))
	a[i][3]=float(input("Dime el factor independiente de la ecuación %d: " % (i+1)))
	print()
	
# imprimiendo datos		
''' for i in range(0,3):
		for j in range(0,4):
			print ("El factor %d de la ecuación %d es: %.2f " % (j+1,i+1,a[i][j]))
'''

# ==================================================================			
# Supongo que el primer factor de cada ecuación es distinto de cero. 
# ==================================================================
for i in range(1,3): # reducción de las ecuaciones 2 y 3 respecto de la primera
	factor = a[i][0]/a[0][0]
	for j in range(0,4):	
		# print("factor: %f" % (factor))
		a[i][j]=a[i][j]-a[0][j]*factor
		
# ecuaciones reducidas 2 y 3
factor = a[2][1]/a[1][1]
for j in range(1,4):
	a[2][j]=a[2][j]-a[1][j]*factor
	
# soluciones
z = a[2][3]/a[2][2]
y = (a[1][3]-a[1][2]*z)/a[1][1]
x = (a[0][3]-a[0][2]*z-a[0][1]*y)/a[0][0]

# imprimiendo datos	
'''	
for i in range(0,3):
	for j in range(0,4):
		print ("El factor %d de la ecuación %d es: %.2f " % (j+1,i+1,a[i][j]))
'''

print ("x=%.2f, y=%.2f y z=%.2f" % (x,y,z))
