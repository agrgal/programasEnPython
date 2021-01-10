# -*- coding: utf-8 -*-

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Tamaño de la letra de la leyenda
mpl.rcParams['legend.fontsize'] = 10

# Inicializo figura
fig = plt.figure()
#  Inicializo AXE . También con ax = fig.gca(projection='3d')
ax = fig.add_subplot(111,projection='3d')

# Creo un array con ángulos. Varias veces 2 PI
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# Creo una serie de puntos en el eje z
z = np.linspace(0, 2, 100)
# Según z, un radio distinto
r = z ** 2 + 1
# Calculo un ángulo
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
