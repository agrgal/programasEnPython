from pygame.locals import *
import os, sys, random
import pygame
import utils
import bullet
import tank
import block

class Level:
  def __init__(self, name, screen):
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.screen = screen
    
    utils.xml_level(self, name)
    
    self.music = "res/music/music_theme_01.mp3"
    
    self.screen.blit(self.background, (utils.margin_menu, 0))
    self.menu = utils.load_image('res/images/others/menuBg.png')
    self.screen.blit(self.menu, (0, 0))
    
    pygame.display.flip()
    
  def prepare_level(self):
    self.user = tank.Tank("user", [utils.margin_menu + self.init_user[0]*32, self.init_user[1]*32], False, None)
    self.block_list = self.generate_borders()
    self.enemies_list = []
    
    for x in range(0, len(self.xml_blocks)):
      block = self.xml_blocks[x]
      pos = [ int(i) for i in block.getAttribute("pos").split(",")]
      name = block.getAttribute("type")
      self.block_list.append(self.generate_blocks(name, pos))
      
    for x in range(0, len(self.xml_enemies)):
      enemy = self.xml_enemies[x]
      pos = [ int(i) for i in enemy.getAttribute("pos").split(",")]
      name = enemy.getAttribute("name")
      self.enemies_list.append(self.generate_enemies(name, pos))
    
  def generate_borders(self):
    l = []
    for i in range(0, 20):
      for j in range(0, 15):
	if i == 0 or j == 0 or i == 19 or j == 14:
	  border_block = block.Block("invencible", (utils.margin_menu + i*32, j*32), self.user)
	  l.append(border_block)
    return l
    
  def generate_blocks(self, name, pos):
    middle_block = block.Block(name, (utils.margin_menu +pos[0]*32, pos[1]*32), self.user)
    return middle_block
    
  def generate_enemies(self, name, pos):
    enemy= tank.Tank(name, [utils.margin_menu +pos[0]*32, pos[1]*32],True, self.user)
    return enemy
      
    
  def show_debug(self):
    font_text = pygame.font.SysFont(pygame.font.get_default_font(), 20)
    surface_text = font_text.render("FPS: " + str(self.clock.get_fps()), True, (255, 0, 0))
    self.screen.blit(surface_text, (0,0))
    surface_text = font_text.render("Tank_level: " + str(self.user.level), True, (255, 0, 0))
    self.screen.blit(surface_text, (0,10))
    
    
  def capture_events(self):
    for event in pygame.event.get():
      if event.type == QUIT:
	exit()
      if event.type == KEYDOWN:
	if event.key == K_SPACE:
	  self.bullets_group.add(self.user.shoot(self.tick))
	if event.key == K_ESCAPE:
	  self.exit = True
	  
  def enemies_shoot(self):
    for e in self.enemies_group:
      if e.shooted:
	if self.tick > e.last_shoot + utils.tick_rate/3:
	  self.bullets_group.add(e.shoot(self.tick))
	  e.shooted = False
	  
  def start(self):
    if utils.musics:
      pygame.mixer.music.load(self.music)
      pygame.mixer.music.play()
    self.prepare_level()
    sprite_list = self.block_list + self.enemies_list + [self.user]
    
    self.bullets_group = pygame.sprite.LayeredUpdates([])
    
    blocks_group = pygame.sprite.RenderUpdates(self.block_list)
    enemies_group = pygame.sprite.RenderUpdates(self.enemies_list)
    sprite_group = pygame.sprite.RenderUpdates(sprite_list)
    
    self.enemies_group = enemies_group
    
    battle_menu = utils.Battle_Menu(self.menu, self.user)
    all_tanks = pygame.sprite.RenderUpdates(self.enemies_list + [self.user])
    self.tick = 0
    self.exit = False
    while not self.exit:
      self.clock.tick_busy_loop(utils.tick_rate)
      self.tick = self.tick + 1
      utils.key_actions(self.user)
      self.capture_events()
      self.enemies_shoot()
      
      ##Collision bullets control
      collides_bullets_blocks = pygame.sprite.groupcollide(self.bullets_group, blocks_group, True, False)
      for m in collides_bullets_blocks:
	m.hit_block(collides_bullets_blocks[m])
      collides_bullets_tanks = pygame.sprite.groupcollide(self.bullets_group, all_tanks, False, False)
      for m in collides_bullets_tanks:
        m.hit_tank(collides_bullets_tanks[m])
        
        
      ##Collision enemies control  
      for m in enemies_group:
	m.collides = []
	collides_enemy_blocks = pygame.sprite.spritecollide(m, blocks_group, False, pygame.sprite.collide_rect)
	m.collides = collides_enemy_blocks
      
      
      ##Collision user control
      collides_user_block = pygame.sprite.spritecollide(self.user, blocks_group, False, pygame.sprite.collide_rect)
      collides_user_tank = pygame.sprite.spritecollide(self.user, enemies_group, False, pygame.sprite.collide_rect)
      self.user.collides = collides_user_block + collides_user_tank
      
      self.bullets_group.update()
      sprite_group.update()
      battle_menu.update()
      
      self.screen.blit(self.background, (160, 0))
      self.screen.blit(self.menu, (0, 0))
      if utils.is_debug:
	self.show_debug()
      self.bullets_group.draw(self.screen)
      sprite_group.draw(self.screen)
      pygame.display.flip()
      if enemies_group.sprites() == []:
	return 1
      if self.user.health < 0:
	return 2
    return 0