# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation

# ================================
# Funciones
# ================================

def introduce(comentario):
	"""
	pre: tamaño del eje, que retornará
	post, 
	"""
	t = True
	while t:
		try:
			x = float(raw_input(comentario+": "))
			if x>0:
				t = False
			elif x<=0:
				print ("No puede ser menor o igual que cero")
		except Exception ,ex:
			print ("No has introducido un dato correcto. Por favor, vuelve a intentarlo:") + str(ex)
	
	return x
	
# ================================
# Programa principal
# ================================
"""	
La tierra se mueve respecto del sol con un movimiento 
elíptico, en el que el sol está en uno de los focos.
El perihelio es la distancia más corta. Unos 147 mill. km.
El afelio es la más larga, unos 152 mill. km
"""
perihelio = introduce("Perihelio (mill. km): ")
afelio = introduce("Afelio (mill. km): ")

if afelio<perihelio:
	print "Te has equivocado. Datos introducidos al revés"

# El semieje focal es la mitad de restar afelio y perihelio
# como no sé si el usuario los ha cambiado, pongo el valor absoluto.
c = np.abs(perihelio-afelio)/2

# Semieje mayor es la semisuma de afelio más perihelio
ejex = (afelio+perihelio)/2
# y con c y a, calculo b, el semieje menor ejey
ejey = np.sqrt(ejex**2 - c **2)
# La excentricidad es la relación entre c y a
excentricidad = c / ejex

print "\nLa distancia focal es 2c=",2*c, " mill. km"
print "\nSemieje menor b=", ejey , " mill. km"
print "\nExcentricidad e=%.3f" % (excentricidad) 

# Resolución del dibujo
resolucion = 0.5
# conjunto de datos x, desde -a hasta a
x = np.arange(-ejex,ejex+resolucion,resolucion)
# conjuntos de datos POSITIVOS en el eje y
y = ejey*np.sqrt(1-(x/ejex)**2)
# Para los datos DEL EJE NEGATIVO Y
# copia de los datos del ejex x, excepto primero y último, y traspuesto
x_menos = x[1:-1][::-1]
# copia de los datos del ejex y, excepto primero y último, y traspuesto
y_menos = -y[1:-1][::-1]

# Uno todos los rangos
x_range = np.concatenate((x, x_menos),axis=0)
y_range = np.concatenate((y, y_menos),axis=0)
# print x_range
# print y_range

# obtengo el número total de puntos que tengo en el array
numpuntos =  np.shape(x_range)[0]
# print numpuntos

# ============================================
# Definición del dibujo y animación
# ============================================

# Defino una figura, y añado un axe (subplot)
# iea rechazada: tamanno_caja = np.maximum(ejex,ejey)*1.05
fig = plt.figure(0)
ax = fig.add_subplot("111",aspect='equal')

#Dibujo de la parte positiva de la trayectoria
plt.plot(x,y,'r-')
#Dibujo de la parte negativa de la trayectoria
plt.plot(x,-y,'r-') #dibuja la otra mitad

# Establezco los límites un 10% más del tamaño de los ejes
ax.set_xlim(-ejex*1.1,ejex*1.1)
ax.set_ylim(-ejey*1.1,ejey*1.1) #límites algo separados.


# Donde se posiciona el SOL
# Posición x del foco, o bien podria haber puesto -c
focox = np.sqrt(ejex**2 - ejey**2)
# Punto de posicionamiento del foco
punto = np.array([-focox,0])
# Definición del patch del SOL
sol = plt.Circle( xy=punto, radius=ejex*0.1) 
# Añado el sol al subplot
ax.add_artist(sol)
# Lo pinto de amarillo
sol.set_facecolor('y')

#====================================================
# Esto es totalmente un truco...
# Dibujo la tierra FUERA DE LA PANTALLA
# Porque...
# Por una parte tiene que estar en el dibujo ANTES DE ANIMARLO.
# Por otra, lo que se quede DIBUJADO antes de llamar a movimiento no se borra
tierra = plt.Circle(xy=(2*ejex,2*ejey) , radius=0.05*ejex) 
ax.add_artist(tierra)
#====================================================

#====================================================
# Movimiento de la tierra
#====================================================

# Una inicialización que no hace nada, pero debe existir para
# los patches
def init():
	return tierra,

# función que calcula el movimiento.
# Parece que itera según i, un contador basado en el frames
def movimiento(i):
	# print i,x_range[i],y_range[i]
	# tierra.radius = ejex * 0.05 #radio tierra
	tierra.center = (x_range[i], y_range[i]) # calculo cada centro del círculo.	
	return tierra,

# Función de animación
anim = animation.FuncAnimation(fig, movimiento, 
                               frames=numpuntos, 
                               init_func = init,
                               interval=100,
                               blit=False)
# Por fin, dibujo.
plt.show()

# ============================================================
# Datos para cálculo
# ============================================================

"""	
Objetos	Afelio	Perihelio
 	millón km (106)	millón km (106)
 	 	 
Mercurio	69.817445	46.001009
Venus	108.942780	 107.476170
Tierra	152.098233	 147.098291
Marte	249.232432 	 206.645215
Ceres	446.428973	380.951528
Júpiter	816.001807	740.679835
Saturno	1503.509229	1349.823615
Urano	3006.318143	2734.998229
Neptuno	4537.039826	4459.753056
Plutón	7376.124302	4436.756954
Makemake	7894.762625	5671.928586
Eris	14594.512904	5765.732799

"""
