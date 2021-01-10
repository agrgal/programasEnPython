import os, sys
import pygame
from pygame.locals import *

import utils

class Bullet(pygame.sprite.Sprite):
  def __init__(self, tank):
    pygame.sprite.Sprite.__init__(self)
    self.tank = tank
    self.pos = [0, 0]
    self.pos[0] = self.tank.pos[0] + 12
    self.pos[1] = self.tank.pos[1] + 12
    self.direction = [0, 0]
    self.damage = tank.damage
    self.speed = 5
    self.image = utils.load_image("res/images/others/bullet.png")
    self.transform_direction(self.tank.head_direction)
    self.rect = self.image.get_rect()

  def transform_direction(self, head):
    if head == 1:
      self.direction[1] = -1
      self.direction[0] = 0
    if head == 3:
      self.direction[1] = 1
      self.direction[0] = 0
      self.image = pygame.transform.rotate(self.image, 180.0)
    if head == 4:
      self.direction[0] = -1
      self.direction[1] = 0
      self.image = pygame.transform.rotate(self.image, 90.0)
    if head == 2:
      self.direction[0] = 1
      self.direction[1] = 0
      self.image = pygame.transform.rotate(self.image, -90.0)
  
  def move(self):
    self.pos[0] = self.pos[0] + self.speed * self.direction[0]
    self.pos[1] = self.pos[1] + self.speed * self.direction[1]
    
  def hit_tank(self, tanks):
    tank = tanks[0]
    if not tank.is_enemy == self.tank.is_enemy:
      tank.health = tank.health - (self.damage - tank.defense*0.5)
      self.kill()
      if tank.health <= 0:
	tank.die()

  def hit_block(self, blocks):
    block = blocks[0]
    if not block.indestructible:
      block.health = block.health - 1
      self.kill()
      if block.health <= 0:
	block.die(self.tank.is_enemy)
    
  def update(self):
    self.move()
    self.rect.center = (self.pos[0], self.pos[1])