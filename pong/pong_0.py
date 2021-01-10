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
