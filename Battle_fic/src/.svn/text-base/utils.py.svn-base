from pygame.locals import *
from xml.dom.minidom import parse
import pygame, os
import random

import game

##Global Variables
is_debug = False
tick_rate = 30
margin_menu = 160
number_of_levels = 2
musics = True
fullscreen = False

def load_image(path):
  try:
    img = pygame.image.load(os.path.realpath(path))
  except pygame.error, message:
    print 'Cannot load image: ', path
    raise SystemExit, message
  img = img.convert()
  return img
  
def load_image_transparent(path):
    image = load_image(path)
    image.set_colorkey(image.get_at((0,0)), RLEACCEL)
    return image
  
def key_actions(user):
  global is_debug
  k = pygame.key.get_pressed()
  if k[pygame.K_F1]:
    pygame.display.toggle_fullscreen()
  if k[pygame.K_F9]:
    is_debug = True
  if k[pygame.K_F8]:
    is_debug = False
  if k[pygame.K_w] or k[pygame.K_UP]:
    user.direction[1] = -1
    user.direction[0] = 0
  elif k[pygame.K_s] or k[pygame.K_DOWN]:
    user.direction[1] = 1
    user.direction[0] = 0
  if k[pygame.K_a] or k[pygame.K_LEFT]:
    user.direction[0] = -1
    user.direction[1] = 0
  elif k[pygame.K_d] or k[pygame.K_RIGHT]:
    user.direction[0] = 1
    user.direction[1] = 0
    
def xml_level(level, name):
  try:
     xmlsource = open(os.path.realpath("data/levels/" + name + ".xml"))
     xml = parse(xmlsource).getElementsByTagName("level")[0]
     xml.enemies = xml.getElementsByTagName("enemies")[0]
     level.xml_enemies = xml.enemies.getElementsByTagName("enemy")
     xml.blocks = xml.getElementsByTagName("blocks")[0]
     level.xml_blocks = xml.blocks.getElementsByTagName("block")
     xml.user = xml.getElementsByTagName("user")[0]
  except pygame.error, message:
    print 'Cannot load xml_tank: '
    raise SystemExit, message
  
  level.name = xml.getAttribute("name")
  level.background = load_image(os.path.realpath(xml.getAttribute("background")))
  level.init_user = [ int(x) for x in xml.user.getAttribute("pos").split(",")]
  

def xml_tank(tank, name):
  try:
     xmlsource = open(os.path.realpath("data/tanks/" + name + ".xml"))
     xml = parse(xmlsource).getElementsByTagName("tank")[0]
     xml.attributes = xml.getElementsByTagName("attributes")[0]
  except pygame.error, message:
    print 'Cannot load xml_tank: '
    raise SystemExit, message
  
  tank.name = xml.getAttribute("name")
  imagesrc = xml.getAttribute("imagesrc")
  tank.image = load_image_transparent(os.path.realpath(imagesrc))
  tank.rect = tank.image.get_rect()
  tank.give_experience = int(xml.attributes.getAttribute("give_experience"))
  tank.speed = int(xml.attributes.getAttribute("speed"))  
  tank.damage = int(xml.attributes.getAttribute("damage"))
  tank.defense = int(xml.attributes.getAttribute("defense"))
  tank.max_health = int(xml.attributes.getAttribute("health"))
  tank.next_level = int(xml.attributes.getAttribute("next_level"))

def xml_block(block, name):
  try:
     xmlsource = open(os.path.realpath("data/blocks/" + name + ".xml"))
     xml = parse(xmlsource).getElementsByTagName("block")[0]
     xml.attributes = xml.getElementsByTagName("attributes")[0]
     xml.images = xml.attributes.getElementsByTagName("image")
  except pygame.error, message:
    print 'Cannot load xml_block: '
    raise SystemExit, message
  
  block.name = xml.getAttribute("name")
  block.indestructible = "True" == xml.attributes.getAttribute("indestructible")
  block.image_list = xml.images
  if block.indestructible:
    block.image = load_image(os.path.realpath(block.image_list[0].getAttribute("src")))
  else:
    block.image = load_image_transparent(os.path.realpath(block.image_list[0].getAttribute("src")))
  block.rect = block.image.get_rect()
  
  block.max_health = int(xml.attributes.getAttribute("health"))  
  block.give_experience = int(xml.attributes.getAttribute("give_experience"))

class Battle_Menu(pygame.surface.Surface):
  def __init__(self, surface, user):
    self.surface = surface
    self.font = pygame.font.get_default_font()
    self.font_text = pygame.font.SysFont(self.font, 20)
    self.avatar = load_image_transparent('res/images/others/avatar_tank.png')
    self.surface.blit(self.avatar, (16, 16))
    self.background = self.surface.copy()
    self.exp_image = load_image('res/images/others/ExpBar.png')
    self.health_image = load_image('res/images/others/lifeBar.png')
    
    self.color = (250, 0, 0)
    self.user = user
    
  def update(self):
    self.reset()
    self.update_health()
    self.update_experience()
    self.write("Damage: ", self.color, (10, 175))
    self.write(str(self.user.damage), self.color, (95, 175))
    self.write("Defense: ", self.color, (10, 215))
    self.write(str(self.user.defense), self.color, (95, 215))
    self.write("Speed: ", self.color, (10, 250))
    self.write(str(self.user.speed), self.color, (95, 250))
    self.write(str(self.user.health) + "/" + str(self.user.max_health), self.color, (70, 300))
    self.write(str(self.user.experience) + "/" + str(self.user.next_level), self.color, (70, 335))
    
  def update_experience(self):
      width = self.user.experience * 128 / self.user.next_level
      self.surface.set_clip(Rect(16, 330, width, 3))
      self.surface.blit(self.exp_image, (16, 330))
      self.surface.set_clip(None)
  
  def update_health(self):
    if self.user.health > 0:
      width = self.user.health * 128 / self.user.max_health
      self.surface.set_clip(Rect(16, 293, width, 3))
      self.surface.blit(self.health_image, (16, 293))
      self.surface.set_clip(None)
    
  def reset(self):
    self.surface.blit(self.background, (0, 0))
    
  def write(self, text, color, pos):
    surface_text = self.font_text.render(text, True, color)
    self.surface.blit(surface_text, pos)
