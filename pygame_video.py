# -*- coding: utf-8 -*-

import pygame, sys, os  
# from pygame import key  
from pygame.display import set_mode  
from pygame import time as pytime 
from pygame.locals import*

pygame.init()  
  
# Le ponemos nombre a la pantalla  
pygame.display.init()
pygame.display.set_caption('Robots')  
  
window = set_mode((640, 640))  

# Paramos mixer, por si acaso estuviese iniciado, ya que da problemas, con el módulo movie  
pygame.mixer.quit()  
# Cargamos el fichero de video  

movie = pygame.movie.Movie('robots.mpg')  

# Le asignamos una pantalla  
movie.set_display(window)  
# Le damos al Play  
movie.play()  
  
pytime.delay(2000)  
exit(0)
