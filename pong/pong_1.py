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

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# 1.- Recibo nombre del archivo e información de transparencia
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
	
	# 3.- Bucle infinito que hace que la ventana se mantenga
	while True:
		# Bucle que comprueba y obtiene la lista de eventos.
		for eventos in pygame.event.get():
			# Si "escucha" un eventos "Cierra ventana", acaba el programa
			if eventos.type == QUIT:
				sys.exit(0)
	# Fin del main
	return 0

if __name__ == '__main__':
	# IMPORTANTE: inicialización de pygame
	pygame.init()
	main()
