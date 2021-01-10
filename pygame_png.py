import pygame  
from pygame.locals import *  
from pygame.display import set_mode  
from pygame import time as pytime 
 
# Le ponemos nombre a la pantalla  
pygame.display.init()  
pygame.display.set_caption('Cochecito')  
window = set_mode((640, 640))   
#Cargamos la imagen del coche  
image = pygame.image.load("coche.png")  
#Redibujamos los elementos de la pantalla  
window.blit(image, (0, 0))  
#Mostramos los cambios de la pantalla  
pygame.display.flip()  
  
pytime.wait(4000)  
exit(0) 
