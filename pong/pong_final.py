#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
# Módulos que se deben cargar
import pygame, sys
from pygame.locals import *


# Constantes
WIDTH = 640 # Ancho de la ventana
HEIGHT = 480 # Alto de la ventana
  
# Clases
# ---------------------------------------------------------------------
""" La clase bola es más que la imagen de una bola; es un sprite
una imagen que interactua, se mueve, etc. La clase bola hereda
los métodos de la clase pygame.sprite.Sprite"""
class Bola(pygame.sprite.Sprite):
	
	# método init
	def __init__(self):
		# llamada la método init de Sprite
		pygame.sprite.Sprite.__init__(self)
		# llamada a la carga de imágenes; con partes transparentes
		self.image = load_image("images/ball.png", True)
		# Obtiene un cuadro que "contiene" a la imagen
		self.rect = self.image.get_rect()
		""" Asigna propiedades importantes, como top, left, bottom, right
		# topleft, bottomleft, topright, bottomright
		# midtop, midleft, midbottom, midright, center, centerx, centery
		# size, width, height, w, h """
		# Defino la pelota en el centro de la pantalla
		self.rect.centerx = WIDTH / 2
		self.rect.centery = HEIGHT / 2
		# Defino la velocidad en los dos ejes, x e y
		self.speed = [0.5, -0.5]
		
	# actualiza el estado de la bola según el tiempo
	def actualizar(self, time, pala_jug, pala_cpu, puntos):
		""" posición de la bola es la posición más velocidad por tiempo
		en cada eje, en el x y en el y"""
		self.rect.centerx += self.speed[0] * time
		self.rect.centery += self.speed[1] * time
		
		# PUNTOS. 
		if self.rect.left <= 0:
			puntos[1] += 1 # toca parte izquierda. Puntos CPU
		if self.rect.right >= WIDTH:
			puntos[0] += 1 	# toca parte derecha. Puntos Jugador	
		
		# Si la parte izquierda es menor que cero 
		# o la derecha mayor que el ancho
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			# cambio el sentido de la velocidad
			self.speed[0] = -self.speed[0]
			# recalculo posición
			self.rect.centerx += self.speed[0] * time
		# lo mismo en el ejey
		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1] * time
		""" comprueba colisiones con el método collide
		si "chocan", cambia la velocidad del mismo """
		if pygame.sprite.collide_rect(self, pala_jug):
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
		
		""" y para la pala de la cpu"""	
		if pygame.sprite.collide_rect(self, pala_cpu):
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0] * time
			
		return puntos
          
# ---------------------------------------------------------------------
""" Defino las palas de juego. Observad que se inicializa con un parámetro
x, ya que habrá que definir el parámetro de los dos"""
			
class Pala(pygame.sprite.Sprite):
	
	def __init__(self, x):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/pala.png")
		self.rect = self.image.get_rect()
		# Ojo, la posición x depende de ese parámetro.
		self.rect.centerx = x
		self.rect.centery = HEIGHT / 2
		# y sól otiene una velocidad
		self.speed = 0.5
	
	# Mover la pala
	def mover(self, time, keys):
		# Si es mayor que cero, admite que se pulse la 
		# tecla arriba, y va restando en función de la velocidad y el tiempo
		if self.rect.top >= 0:
			if keys[K_UP]:
				self.rect.centery -= self.speed * time
		  # lo contrario, si es menor que la altura, suma si la tecla abajo está presionada 
		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed * time
	""" Método que mueve la pala automáticamente, en función
	de la bola"""			
	def ia(self, time, ball):
		# Si la velocidad es positiva, se mueve a la derecha
		# y sobrepasa la mitad del tablero
		if ball.speed[0] >= 0 and ball.rect.centerx >= WIDTH/2:
			# Si la posición y es menor que la posición y de la bola
			# aumenta la posición y de la pala
			if self.rect.centery < ball.rect.centery:
				self.rect.centery += self.speed * time
			# y al contario
			if self.rect.centery > ball.rect.centery:
				self.rect.centery -= self.speed * time

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
	
	# 1.- Comando para crear una ventana de alto y ancho..
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	# 2.- Título de la ventana
	pygame.display.set_caption("Pruebas Pygame")
	
	# 4.- Carga de imágenes de fondo
	background_image = load_image('images/fondo_pong.png') 
	
	# 7.- crear una bola
	bola=Bola()
	
	# 12.- Pala del jugador
	pala_jug=Pala(30)
	# 17.- Pala del ordenador
	pala_cpu=Pala(WIDTH-30)
	
	# 21.- Puntos, inicialziar
	puntos = [0,0]
	
	# 9.- Crear un reloj. Antes de la iteración
	clock = pygame.time.Clock()
	
	# 3.- Bucle infinito que hace que la ventana se mantenga
	while True:
		
		# 10.- tiempo que ha pasado en cada iteración
		time = clock.tick(60) # 60 es el framerate, para que funciones
		# igual en todos los ordenadores
		
		# 14.- comprueba si se ha pulsado una tecla. Obtiene variable KEYS
		keys = pygame.key.get_pressed()
		
		# Bucle que comprueba y obtiene la lista de eventos.
		for eventos in pygame.event.get():
			# Si "escucha" un eventos "Cierra ventana", acaba el programa
			if eventos.type == QUIT:
				sys.exit(0)
				
		# 5.- Coloco la imagen de fondo en la esquina superior izquierda
		screen.blit(background_image, (0, 0)) 
		# 8.- Poner la bola en la ventana
		screen.blit(bola.image, bola.rect) # en el lugar definido por sus coordenadas
		# 13.- Poner la pala en la pantalla
		screen.blit(pala_jug.image, pala_jug.rect)
		# 18.- Poner en pantalla la pala de la cpu
		screen.blit(pala_cpu.image, pala_cpu.rect)
		
		# ACTUALIZACIONES
		# 11.- Actualizo la bola ANTES de actualizar la ventana
		# bola.actualizar(time, pala_jug, pala_cpu) # 16.- Modificar y añadir pala_jug # 19.- pala cpu
		puntos = bola.actualizar(time, pala_jug, pala_cpu, puntos) # 21.-  control de la puntuación
		# 15.- Método mover la pala del jugador
		pala_jug.mover(time, keys)
		# 20.- Inteligencia artificial: mover pala cpu
		pala_cpu.ia(time,bola) # necesita conocer dónde está la bola
		
		# 22.- Puntos en el caption
		cadena = "Pygame PONG. Tanteador (%d,%d)" % (puntos[0],puntos[1])
		pygame.display.set_caption(cadena)
		
		# 6.- Actualizo la ventana
		pygame.display.flip() 
		
	# Fin del main
	return 0

if __name__ == '__main__':
	# IMPORTANTE: inicialización de pygame
	pygame.init()
	main()
