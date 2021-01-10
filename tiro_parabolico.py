# *-* coding: utf-8 *-*
import visual as vs
import numpy as np
## valores iniciales (modifícalos bajo tu responsabilidad)
v0 = 80 ## v en m/s
alfa = 60 ## ángulo en grados
vel_fotogramas = 15  ## la velocidad del video
## Constantes
g = 9.81 ## Aceleración de la gravedad
## ecuaciones
v0x = v0 * np.cos(np.deg2rad(alfa))
v0z = v0 * np.sin(np.deg2rad(alfa))
t_total = 2 * v0z / g
x_final = v0x * t_total
## Empezamos con visual python (vpython)
## Creamos el 'suelo'
suelo = vs.box(pos = (x_final/2., -1, 0),
               size = (x_final, 1, 10), color = vs.color.green)
## Creamos el 'cañón'
canyon = vs.cylinder(pos = (0, 0, 0),
                     axis = (2 * np.cos(np.deg2rad(alfa)), 2 * np.sin(np.deg2rad(alfa)), 0))
## Creamos el proyectil y una línea que dejará la estela del proyectil
bola = vs.sphere(pos = (0, 0, 0))
bola.trail = vs.curve(color=bola.color)
## Creamos la flecha que indica la dirección del movimiento (vector velocidad)
flecha = vs.arrow(pos = (0, 0, 0),
                  axis = (v0x, v0z, 0), color = vs.color.yellow)
## texto (ponemos etiquetas para informar de la posición del proyectil)
labelx = vs.label(pos = bola.pos, text= 'posicion x = 0 m', xoffset=1,
                  yoffset=80, space=bola.radius, font='sans', box = False,
                  height = 10)
labely = vs.label(pos = bola.pos, text= 'posicion y = 0 m', xoffset=1,
                  yoffset=40, space=bola.radius, font='sans', box = False,
                  height = 10)
## Animamos todo el cotarro!!!
t = 0
while t <= t_total:
    bola.pos = (v0x * t, v0z * t - 0.5 * g * t**2, 0)
    flecha.pos = (v0x * t, v0z * t - 0.5 * g * t**2, 0)
    flecha.axis = (v0x, v0z - g * t, 0)
    bola.trail.append(pos=bola.pos)
    labelx.pos = bola.pos
    labelx.text = 'posicion x = %s m' % str(v0x * t)
    labely.pos = bola.pos
    labely.text = 'posicion y = %s m' % str(v0z * t - 0.5 * g * t**2)
    t = t + t_total / 100.
    vs.rate(vel_fotogramas)