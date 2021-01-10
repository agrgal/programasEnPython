# -*- coding: utf-8 -*-

import pygame, sys, os  
from pygame import key  
# from pygame.display import set_mode  
from pygame import time as pytime 
from pygame.locals import*


# Inicializamos  
pygame.mixer.init()  
# Cargamos la cancion  
pygame.mixer.music.load("musica.mp3")  
# Le damos al Play  
pygame.mixer.music.play()  
# Esperamos un tiempo a que acabe la cancion  
pytime.wait(110000) # En milisegundos
# Salimos del programa  
exit(0)
