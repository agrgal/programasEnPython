import os, sys, random
import pygame
from pygame.locals import *

import bullet
import utils

class Tank(pygame.sprite.Sprite):
  def __init__(self, type_tank, pos, is_enemy, user):
    pygame.sprite.Sprite.__init__(self)
    utils.xml_tank(self, type_tank)
    self.pos = [x+3 for x in pos]
    self.level = 1
    self.experience = 0
    self.health = self.max_health
    self.collides = []
    self.direction = [0, 0]
    self.head_direction = 1
    self.is_enemy = is_enemy
    self.user = user
    self.shooted = False
    self.last_shoot = 0
    
  def update(self):
    if self.is_enemy:
      self.get_direction() #Enemy method
      self.get_shoot() #Enemy method
    self.flip_image()
    self.prepare_move()
    self.next_lvl()
    self.move()
    self.rect.topleft = (self.pos[0], self.pos[1])
    
  def get_direction(self):
    self.direction = [0, 0]
    if self.pos[0] < self.user.pos[0]:
      self.direction[0] = 1
    elif self.pos[0] - 24 > self.user.pos[0]:
      self.direction[0] = -1
    if self.direction[0] == 0:
      if self.pos[1] < self.user.pos[1]:
	self.direction[1] = 1
      elif self.pos[1] - 24 > self.user.pos[1]:
	self.direction[1] = -1
	  
  def get_shoot(self):
    for z in [0, 1]:
      if self.user.pos[z] - 12 <= self.pos[z] <= self.user.pos[z] + 12:
	self.shooted = True
    
  def prepare_move(self):
    for f in self.collides:
      if not f.alive: continue
      for z in [0, 1]:
	if self.pos[z] < f.pos[z] and self.pos[z] + 32 > f.pos[z] and self.direction[z] == 1:
		self.pos[z] = self.pos[z] - self.speed
		self.direction[z] = 0
	if self.pos[z] > f.pos[z] and self.pos[z] - 32 < f.pos[z] and self.direction[z] == -1:
		self.pos[z] = self.pos[z] + self.speed
		self.direction[z] = 0
        
  def next_lvl(self):
    if self.experience >= self.next_level:
      att = random.randint(1, 3)
      if att == 1:
	    self.damage = self.damage + 1
      if att == 2:
	    self.speed = self.speed + 1
      if att == 3:
	    self.defense = self.defense + 1
	
      next_level = self.next_level
      self.next_level = 2 * self.next_level * self.level
      self.experience = self.experience - next_level
      self.level = self.level + 1
  
  def move(self):
    self.pos[0] = self.pos[0] + self.speed * self.direction[0]
    self.pos[1] = self.pos[1] + self.speed * self.direction[1]
  
  def calculate_head(self):
    if not self.direction == [0, 0]:
      if self.direction == [0, -1]:
	return 1
      elif self.direction == [0, 1]:
	return 3
      elif self.direction == [-1, 0]:
	return 4
      elif self.direction == [1, 0]:
	return 2
    return 0
  
  def flip_image(self):
    head = self.calculate_head()
    x = self.head_direction
    if not head == 0:
      if head-x%4 == 2 or head-x%4 == -2:
	self.image = pygame.transform.rotate(self.image, 180.0)
	self.head_direction = head
      if head-x%4 == 1 or head-x%4 == -3:
	self.image = pygame.transform.rotate(self.image, -90.0)
	self.head_direction = head
      if head-x%4 == 3 or head-x%4 == -1:
	self.image = pygame.transform.rotate(self.image, 90.0)
	self.head_direction = head
	
  def die(self):
    if self.is_enemy and not self.user == None :
      self.user.experience = self.user.experience + self.give_experience
      self.kill()
	
  def shoot(self, last_shoot):
    self.last_shoot = last_shoot
    return [bullet.Bullet(self)]
    
    