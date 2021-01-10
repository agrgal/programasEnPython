# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Ellipse

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
		
ejex = introduce("Tamaño del eje X")
ejey = introduce("Tamaño del eje Y")

x = np.arange(-ejex,ejex+0.001,0.001)
y = ejey*np.sqrt(1-(x/ejex)**2)

tamanno_caja = np.maximum(ejex,ejey)*1.05

fig = plt.figure(1)

sp1 = plt.subplot(121)
plt.plot(x,y,'r-')
plt.plot(x,-y,'r-') #dibuja la otra mitad

# Comparando con la elipse que dibuja matplotlib
centro=np.array([0,0])

sp2 = plt.subplot(122)
elip = Ellipse(xy=centro, width=2*ejex, height=2*ejey, angle=0.0)
sp2.add_artist(elip)
elip.set_clip_box(sp2.bbox)

# límites
sp1.set_xlim(-tamanno_caja, tamanno_caja)
sp1.set_ylim(-tamanno_caja, tamanno_caja)
sp2.set_xlim(-tamanno_caja, tamanno_caja)
sp2.set_ylim(-tamanno_caja, tamanno_caja)

plt.show()


