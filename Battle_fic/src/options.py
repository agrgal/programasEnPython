from pygame.locals import *
import os, sys, random
import pygame

import utils
import level

class Options():
  def __init__(self, screen):
    self.screen = screen
    self.load_all_images()
    self.bg_copy = self.bg
    self.screen.blit(self.bg, (0,0))
    pygame.display.flip()
    
  def load_all_images(self):
    self.bg = utils.load_image("res/images/backgrounds/mainMenuBg.png")
    self.menu = utils.load_image("res/images/others/optionsMenu_Options.png")
    self.menu_selected = utils.load_image("res/images/others/optionsMenu_Options_OverSelect.png")
  def capture_events(self):
    for event in pygame.event.get():
      if event.type == QUIT:
	exit()
      if event.type == KEYDOWN:
	if event.key == K_ESCAPE:
	  exit()
      if event.type == MOUSEBUTTONDOWN:
	m = pygame.mouse.get_pressed()
	if m == (1, 0, 0):
	  self.check_select()
	 
  def check_select(self):
    if self.select == 1:
      utils.musics = True
      pygame.mixer.init()
    if self.select == 2:
      utils.musics = False
      pygame.mixer.quit()
    if self.select == 3:
      utils.fullscreen = True
      pygame.display.toggle_fullscreen()
    if self.select == 4:
      utils.fullscreen = False
      pygame.display.toggle_fullscreen()
    if self.select == 5:
      self.back = True
  
  def menu_select(self):
    mouse_pos = pygame.mouse.get_pos()
    if 200 < mouse_pos[0] < 600:
      if 115 <= mouse_pos[1] < 165:
	self.select = 1
	return
      if 165 <= mouse_pos[1] < 215:
	self.select = 2
	return
      if 215 <= mouse_pos[1] < 265:
	self.select = 3
	return
      if 265 <= mouse_pos[1] < 315:
	self.select = 4
	return
      if 315 <= mouse_pos[1] < 365:
	self.select = 5
	return
    self.select = 0
	
  def real_draw(self, left, top, weigth):
    self.bg.set_clip(Rect(left, top, weigth, 50))
    self.bg.blit(self.menu_selected, (200, 115))
    self.bg.set_clip(None)

  def draw_select(self):
    if utils.musics:
      self.real_draw(460, 115, 140)
    else:
      self.real_draw(460, 165, 140)
    if utils.fullscreen:
      self.real_draw(500, 215, 100)
    else:
      self.real_draw(500, 265, 100)
    if not self.select == 0:
      top = 65 + 50*self.select
      self.bg.set_clip(Rect(200, top, 400, 50))
      self.bg.blit(self.menu_selected, (200, 115))
      self.bg.set_clip(None)
      
  def start(self):
    self.back = False
    while not self.back:
      self.capture_events()
      self.bg.blit(self.menu, (200,115))
      self.menu_select()
      self.draw_select()
      self.screen.blit(self.bg, (0,0))
      self.bg = self.bg_copy
      pygame.display.flip()
    return
    