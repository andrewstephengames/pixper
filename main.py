import pygame
import random
import math
import os

from pygame import mixer

#pygame.mixer.pre_init(44100, 16, 2, 4096)
# initialize pygame
pygame.init ()
#pygame.mixer.init()

# window stuff

width = 800
height = 600

# create the screen
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# set title and icon
pygame.display.set_caption ("Pixper")
icon = pygame.image.load("res/player.png")
pygame.display.set_icon (icon)

# background

#bgImg = pygame.image.load("res/background.jpg")

# tiles
grassImg = pygame.image.load ("res/grass.png")

# player

playerImg = pygame.image.load("res/player-black.png")
enemyImg = pygame.image.load("res/enemy-black.png")
playerX = random.randint (0, 800)
playerY = random.randint (0, 600)
playerSpeed = 10

# enemy

enemyX = random.randint (0, 800)
enemyY = random.randint (0, 600)
enemySpeed = 3

# sounds

hurtSound = pygame.mixer.Sound ("res/sounds/oof.ogg")

# handle keys

keys = {'w': False,'a': False,'s': False,'d': False}
     
# entities

def player(x, y):
     screen.blit(playerImg, (x, y))
def enemy(x, y):
     screen.blit(enemyImg, (x, y))
     global playerX, playerY, enemyX, enemyY
     global enemySpeed
     if enemyX < playerX:
          enemyX += enemySpeed
     else: enemyX -= enemySpeed
     if enemyY < playerY:
          enemyY += enemySpeed
     else: enemyY -= enemySpeed
     
def isCollision (x1, y1, x2, y2):
     distance = math.sqrt(math.pow(x2-x1, 2) + math.pow (y2-y1, 2))
     return distance < 5

# gameloop
running = True
while running:
     screen.fill ((0, 0, 0))
     #screen.blit (bgImg, (0, 0))
     screen.blit (grassImg, (0, 0))
     for event in pygame.event.get():
          # if screen gets resized adjust window size, entity speeds          
          if event.type == pygame.VIDEORESIZE:
               width = screen.get_width()
               height = screen.get_height()
               playerSpeed *= 2*(width/height)
               enemySpeed *= 2*(width/height)
               #screen.blit (grassImg, (0, 0))
               pygame.display.update()
          if event.type == pygame.QUIT:
               running = False
          # if keystroke is pressed, check which one
          if event.type == pygame.KEYDOWN:
               pygame.key.set_repeat(15)
               if event.key == pygame.K_w:
                    keys['w'] = True
               if event.key == pygame.K_a:
                    keys['a'] = True
               if event.key == pygame.K_s:
                    keys['s'] = True
               if event.key == pygame.K_d:
                    keys['d'] = True
               if event.key == pygame.K_q:
                    running = False
          elif event.type == pygame.KEYUP:
               if event.key == pygame.K_w:
                    keys['w'] = False
               if event.key == pygame.K_a:
                    keys['a'] = False
               if event.key == pygame.K_s:
                    keys['s'] = False
               if event.key == pygame.K_d:
                    keys['d'] = False
               
     if keys['w']:
          playerY -= playerSpeed
     if keys['a']:
          playerX -= playerSpeed
     if keys['s']:
          playerY += playerSpeed
     if keys['d']:
          playerX += playerSpeed
                    
     # rgb
     if playerX <= 0:
          playerX = 0
     if playerX >= width-32:
          playerX = width-32
     if playerY <= 0:
          playerY = 0
     if playerY >= height-32:
          playerY = height-32
     if enemyX <= 0:
          enemyX = 0
     if enemyX >= width-32:
          enemyX = width-32
     if enemyY <= 0:
          enemyY = 0
     if enemyY >= height-32:
          enemyY = height-32

     
     # collision

     collision = isCollision (playerX, playerY, enemyX, enemyY)
     if collision:
          print ("Player and enemy have collided!")
          hurtSound.play()
          running = False 
     
     player(playerX, playerY)
     enemy (enemyX, enemyY)
     pygame.display.update()
