#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
# Módulos que se deben cargar
import pygame
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
	
	# 3.- Bucle infinito que hace que la ventana se mantenga
	while True:
		# Bucle que comprueba y obtiene la lista de eventos.
		for eventos in pygame.event.get():
			# Si "escucha" un eventos "Cierra ventana", acaba el programa
			if eventos.type == QUIT:
				sys.exit(0)
				
		# 5.- Coloco la imagen de fondo en la esquina superior izquierda
		screen.blit(background_image, (0, 0)) 
		# 6.- Actualizo la ventana
		pygame.display.flip() 
		
	# Fin del main
	return 0

if __name__ == '__main__':
	# IMPORTANTE: inicialización de pygame
	pygame.init()
	main()
