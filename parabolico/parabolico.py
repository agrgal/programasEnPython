#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame, sys, math, random
from pygame.locals import *

# Constantes
ALTO = 600
ANCHO = 800
VINI = 800
PI = 4*math.atan(1)
# Los límites en los ejes
LIMITEX = 32000 #640000 es el alcance máximo a 45º, pero debo poner
# los límites iguales para que sea creíble, así que 35000
LIMITEY = 32000 # 31668 altura maxima para un disparo de 80º
# ¡Atención! Limito los ángulos entre 5 y 80 grados

# Clases
# ---------------------------------------------------------------------
class Cannon(pygame.sprite.Sprite):	
	# método init
	def __init__(self):
		# llamada la método init de Sprite
		pygame.sprite.Sprite.__init__(self)
		#  Dibuja un rectángulo alargado. True para conservar transparencia
		self.cargar()
		self.angle = 5
		# print self.rect.w, self.rect.h
	
	def cargar(self):
		# Al inicio o cuando gira, recarga la imagen
		self.image = load_image("imagenes/canon3.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = 10+10
		self.rect.centery = ALTO-10
	
	#colocar imagen rotada
	def colocar(self):
		self.cargar()
		# proceso de copia de imagen
		orig_rect = self.rect
		imagen = pygame.transform.rotate(self.image,self.angle)
		rot_rect =orig_rect.copy()
		rot_rect.center = imagen.get_rect().center
		imagen = imagen.subsurface(rot_rect).copy()
		self.image = imagen
		# print self.rect.centerx, self.rect.centery, self.rect.w, self.rect.h, self.angle
		
	def actualizar(self, time, keys, estado):
		if estado == 1:
			return # no puedo mover el cañón hasta que el disparo anterior no termine
		if keys[K_UP]:
			self.angle += 0.005*time	
			if self.angle > 80:
				self.angle = 80
			self.colocar()		
			pygame.time.delay(150) # retraso para un mejor movimiento con los cursores
		# lo contrario, si es menor que la altura, suma si la tecla abajo está presionada 
		if keys[K_DOWN]:
			self.angle -= 0.005*time
			if self.angle < 5:
				self.angle = 5
			self.colocar()
			pygame.time.delay(150) # retraso para un mejor movimiento con los cursores.
		# print self.angle	

# ---------------------------------------------------------------------
# Clase BALA
# ---------------------------------------------------------------------		
class Bala(pygame.sprite.Sprite):	
	# método init
	def __init__(self):
		# llamada la método init de Sprite
		pygame.sprite.Sprite.__init__(self)
		#  Dibuja un rectángulo alargado. True para conservar transparencia
		self.coordx = 0 # coordenada tiro parabólico
		self.coordy = 0 # coordenada tiro parabólico
		self.tiempo = 0 # cuenta de tiempo
		self.cargar()
		self.angle = 5
		# print self.rect.w, self.rect.h
	
	def cargar(self):
		# Al inicio o cuando gira, recarga la imagen
		self.image = load_image("imagenes/CannonBall.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = 10+10+200
		self.rect.centery = ALTO-10-200
		
	def parametros(self, angulo):
		self.tmax = 2 * VINI * math.sin(angulo*PI/180) / 9.8
		self.alcance = VINI * math.cos(angulo*PI/180) * self.tmax
		
	def actualizar(self, time, angulo, diana):

		# Llamamos continuamente a la bola, que irá disparando
		# coordenadas del tiro parabólico
		self.coordx = VINI * math.cos(angulo*PI/180) * self.tiempo
		self.coordy = VINI * math.sin(angulo*PI/180) * self.tiempo - 4.9 * (self.tiempo ** 2)
		self.tiempo += 1 # por cada segundo.
		# transformo coordenadas a píxeles
		self.rect.centerx = 10 + (self.coordx * (ANCHO-15))/ (LIMITEX)
		self.rect.centery = ALTO - 10 -  (self.coordy * (ALTO-15))/ (LIMITEY)
		# retraso
		# print self.tiempo, self.coordx, self.coordy, self.rect.centerx, self.rect.centery
		pygame.time.delay(20)		
				
		# Detectando colisiones. Si alcanza devuelve 1, si no, cero	
		# defino dos áreas, centradas donde están las de la bala y la de la diana	
		bala_rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
		di_rect = diana.image.get_rect(center=(diana.rect.centerx,diana.rect.centery))
		# haga más pequeñas esas áreas. En 15 y 25 puntos respectivamente.
		bala_rect = bala_rect.inflate(-15,-15)
		di_rect = di_rect.inflate(-25,-25)
		# Si las áreas se solapan, entonces hay colisión.
		if di_rect.colliderect(bala_rect):
			# print bala_rect,di_rect
			return 1
		else:
			return 0
			
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------
# Clase DIANA
# ---------------------------------------------------------------------		
class Diana(pygame.sprite.Sprite):	
	# método init
	def __init__(self):
		# llamada la método init de Sprite
		pygame.sprite.Sprite.__init__(self)
		self.cargar()
		
	def cargar(self):
		self.image = load_image("imagenes/diana.png",True)
		self.rect = self.image.get_rect()
		self.rect.centerx = random.randint(100,ANCHO-20)
		self.rect.centery = random.randint(100,ALTO-100)		

# ---------------------------------------------------------------------



# Funciones
# ---------------------------------------------------------------------
# F1.- Recibo nombre del archivo e información de transparencia
def load_image(filename, transparent=False):
	try:
		# 2.- Carca la imagen
		image = pygame.image.load(filename)
	except pygame.error, message:
		# propaga mensaje de error
		raise SystemExit, message
		# 3.- Convierte al tipo interno de imagen de Pygame (más eficiente)
	image = image.convert()
	if transparent:
		"""
		Esta línea es un condicional que controla si el parametro 
		transparent es verdadero y en caso afirmativo ejecuta las siguientes lineas
		, la primera obtiene el color del pixel (0, 0) de la imagen 
		(esquina superior izquierda) y la otra  lo define como 
		color transparente de la imagen. Es decir que si quieres una 
		imagen con transparencia, el color que actua como transparente 
		se toma del pixel superior izquierdo, 
		asi que asegurate que este color no esta en la imagen. 
		"""
		color = image.get_at((0,0))
		image.set_colorkey(color, RLEACCEL)
	return image
	
# ---------------------------------------------------------------------

def main():

	""" ===================== """	
	""" Condiciones iniciales """
	""" ===================== """
	# 1.- Comando para crear una ventana de alto y ancho..
	screen = pygame.display.set_mode((ANCHO, ALTO))
	# 2.- Título de la ventana
	pygame.display.set_caption("Tiro parabólico")
	# 3.- Crear un reloj. Antes de la iteración
	clock = pygame.time.Clock()
	# 4.- Listado de colores
	blanco=(255,255,255)
	
	# 5.- Dibujo de los ejes de coordenadas
	pygame.draw.lines(screen,blanco,False,[(5,ALTO-10),(ANCHO-5,ALTO-10)],3) #eje X
	pygame.draw.lines(screen,blanco,False,[(10,5),(10,ALTO-5)],3) #eje Y
	# Transformación PIXELES --> METROS  x = 10 ** 4 * (pix_x -10) / (ANCHO-15)
	# Y en el eje Y: y = (ALTO - 10) - 10 ** 4 (pix_y - 10) / (ALTO -15)
	for i in range(5,ANCHO-5,10): #Marcas en el eje X
		pygame.draw.lines(screen,blanco,False,[(i,ALTO-8),(i,ALTO-12)],2)
	for j in range(5,ALTO-10,10): #Marcas en el eje Y
		pygame.draw.lines(screen,blanco,False,[(8,j),(12,j)],2)
		
	# Hacer una copia de una zona de la pantallaz
	# zona_rect = pygame.Rect(0,ALTO-120,120,120)
	# zona_rect = pygame.Rect(180,ALTO-10-230,60,60)
	# zona = screen.subsurface(zona_rect)
	# zona.fill(blanco) #Uso para localizar la zona visualmente
	# zona = zona.convert() #hay que acabar dibujando esta línea
	# Pero acabo redibujando el fondo
	zona_rect = pygame.Rect(0,0,ANCHO,ALTO) # después de dibujada
	zona = screen.subsurface(zona_rect)
	zona = zona.convert()
	
	# 7.- Definir SPRITES
	canon = Cannon()
	diana = Diana()
	canon.colocar()
	
	# IMPORTANTE: variable estado. Estado es 0 cuando aún no se ha 
	# disparado, y 1 si se ha disparado.
	estado = 0 # Estado de no disparo
	
	""" =========================== """	
	""" Bucle del programa pincipal """
	""" =========================== """
	while True:
		
		# 4.- tiempo que ha pasado en cada iteración
		time = clock.tick(60) # 60 es el framerate, para que funciones
		# igual en todos los ordenadores		
		# 5.- comprueba si se ha pulsado una tecla. Obtiene variable KEYS
		keys = pygame.key.get_pressed()		
	
		# Bucle que comprueba y obtiene la lista de eventos.
		for eventos in pygame.event.get():
			# Si "escucha" un evento "Cierra ventana", acaba el programa
			if eventos.type == QUIT:
				sys.exit(0)
			if (keys[K_SPACE] and estado == 0): # comprobar estado evita 
				# disparar hasta que el otro disparo termine
				estado = 1
				bala = Bala()
				bala.parametros(canon.angle)
		
		#Actualizo fondo
		screen.blit(zona, zona_rect)
		
		# Actualizo el cañón
		canon.actualizar(time,keys,estado)
		
		# Colocar SPRITES en la ventana. X, Y, y ángulo de giro
		screen.blit(canon.image, canon.rect) # en el lugar definido por sus coordenadas	
		screen.blit(diana.image, diana.rect) # coloco la diana
		
		# Para disparar la bala	
		if estado == 1:
			alcanzado = bala.actualizar(time, canon.angle, diana) # se actualiza la bala
			if (bala.coordy>=0 and bala.rect.centerx<=ANCHO and alcanzado==0):
				# Se deben dar tres condiciones: que la bala no caiga al suelo, 
				# Que no sobrepase la pantalla
				# Que no haya tocado la diana
				print bala.rect.centerx
				screen.blit(bala.image, bala.rect) # en el lugar definido por sus coordenadas			
			else:
				pygame.time.delay(500) # Algo de espera
				diana.cargar() # Una nueva posición de la diana
				estado = 0				
			
				
			
		
		# refresca la pantalla
		pygame.display.flip()
		
	""" ========================== """	
	""" Fin del programa principal """
	""" ========================== """
	return 0

if __name__ == '__main__':
	# IMPORTANTE: inicialización de pygame
	pygame.init()
	main()
