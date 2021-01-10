from pygame.locals import *
import os, sys, random, time
import pygame

import utils
import level
import options

class Game():
  def __init__(self):
    pygame.display.set_caption('Battle FIC')
    self.screen = pygame.display.set_mode((800, 480))
    self.load_all_images()
    pygame.display.set_icon(self.icon)
    
    self.screen.blit(self.bg, (0,0))
    self.bg_copy = self.bg
    pygame.display.flip()
    self.select = 1
    
  def load_all_images(self):
    self.icon = utils.load_image("res/images/others/battleFic_icon.png")
    self.bg = utils.load_image("res/images/backgrounds/mainMenuBg.png")
    self.menu = utils.load_image("res/images/others/mainMenu_Options.png")
    self.menu_selected = utils.load_image("res/images/others/mainMenu_Options_OverSelect.png")
    self.win = utils.load_image("res/images/backgrounds/youWin.png")
    self.lose = utils.load_image("res/images/backgrounds/youLose.png")
    
  def capture_events(self):
    for event in pygame.event.get():
      if event.type == QUIT:
	exit()
      if event.type == KEYDOWN:
	if event.key == K_ESCAPE:
	  exit()
	if event.key == K_UP:
	  if not self.select == 1:
	    self.select = self.select - 1
	if event.key == K_DOWN:
	  if not self.select == 3:
	    self.select = self.select + 1
	if event.key == K_SPACE or event.key == K_RETURN:
	  self.check_select()
      if event.type == MOUSEBUTTONDOWN:
	m = pygame.mouse.get_pressed()
	if m == (1, 0, 0):
	  self.check_select()
	 
  def check_select(self):
    if self.select == 1:
      fin =  True
      num = 1
      while fin:
	l = level.Level('level_' + str(num), self.screen)
	control = l.start()
	num = num + 1
	if control == 1:
	  if num > utils.number_of_levels:
	    self.win_lose(True)
	    pygame.mixer.music.stop()
	    fin = False
	elif control == 2:
	  self.win_lose(False)
	  fin = False
	  pygame.mixer.music.stop()
	elif control == 0:
	  fin = False
	  pygame.mixer.music.stop()
    if self.select == 2:
      options.Options(self.screen).start()
    if self.select == 3:
      exit()
  
  def menu_select(self):
    mouse_pos = pygame.mouse.get_pos()
    if 200 < mouse_pos[0] < 600:
      if 165 <= mouse_pos[1] < 215:
	self.select = 1
      if 215 <= mouse_pos[1] < 265:
	self.select = 2
      if 265 <= mouse_pos[1] < 315:
	self.select = 3

  def draw_select(self):
    if not self.select == 0:
      top = 115 + 50*self.select
      self.bg.set_clip(Rect(200, top, 400, 50))
      self.bg.blit(self.menu_selected, (200, 165))
      self.bg.set_clip(None)
      
  def win_lose(self, winlose):
    if winlose:
      self.screen.blit(self.win, (0, 0))
      pygame.display.flip()
    else:
      self.screen.blit(self.lose, (0, 0))
      pygame.display.flip()
    time.sleep(2)
    self.screen.blit(self.bg, (0,0))
    pygame.display.flip()
  
  def start(self):
    control = True
    while 1:
      self.capture_events()
      self.bg.blit(self.menu, (200,165))
      self.menu_select()
      self.draw_select()
      self.screen.blit(self.bg, (0,0))
      self.bg = self.bg_copy
      pygame.display.flip()
	
if __name__ == "__main__":
  Game().start()
    
