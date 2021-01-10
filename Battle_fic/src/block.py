import os, sys
import pygame
from xml.dom.minidom import parse
from pygame.locals import *

import utils

class Block(pygame.sprite.Sprite):
  def __init__(self, type_block, pos, user):
    pygame.sprite.Sprite.__init__(self)
    utils.xml_block(self, type_block)
    self.health = self.max_health
    self.pos = pos
    self.user = user
    #self.rect.topleft = self.pos
    
  def transform_direction(direction):
    if direction == 1:
      return [0. -1]
    if direction == 2:
      return [1, 0]
    if direction == 3:
      return [0, 1]
    if direction == 4:
      return [-1, 0]
    return [0, 0]
  
  def update(self):
    self.rect.topleft = self.pos
    if not self.indestructible:
      self.change_image()
    
  def die(self, no_user):
    if not no_user:
      self.user.experience = self.user.experience + self.give_experience
    self.kill()
    
  def change_image(self):
    new_image = (self.max_health - self.health)
    if len(self.image_list) >= new_image:
      self.image = utils.load_image_transparent(os.path.realpath(self.image_list[new_image].getAttribute("src")))