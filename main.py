import pygame
import random

# initialize pygame
pygame.init ()

# create the screen
screen = pygame.display.set_mode((800, 600))

# set title and icon
pygame.display.set_caption ("Pixper")
icon = pygame.image.load("res/player.png")
pygame.display.set_icon (icon)

# player

playerImg = pygame.image.load("res/player.png")
enemyImg = pygame.image.load("res/enemy.png")
playerX = random.randint (0, 800)
playerY = random.randint (0, 600)
playerSpeed = 5

# enemy

enemyX = random.randint (0, 800)
enemyY = random.randint (0, 600)

def player(x, y):
     screen.blit(playerImg, (x, y))
def enemy(x, y):
     screen.blit(enemyImg, (x, y))

# gameloop
running = True
while running:
     for event in pygame.event.get():
          Wpress = False
          Apress = False
          Spress = False
          Dpress = False
          if event.type == pygame.QUIT:
               running = False
          # if keystroke is pressed, check which one
          if event.type == pygame.KEYDOWN:
               pygame.key.set_repeat(20)
               if event.key == pygame.K_w:
                    playerY -= playerSpeed
                    Wpress = True
               if event.key == pygame.K_a:
                    playerX -= playerSpeed
                    Apress = True
               if event.key == pygame.K_s:
                    playerY += playerSpeed
                    Spress = True
               if event.key == pygame.K_d:
                    playerX += playerSpeed
                    Dpress = True
     if Apress and Wpress:
       playerY -= playerSpeed
       playerX -= playerSpeed
     if Spress and Dpress:
       playerY += playerSpeed
       playerX += playerSpeed
     if Wpress and Dpress:
       playerY -= playerSpeed
       playerX += playerSpeed
     if Apress and Spress:
       playerX -= playerSpeed
       playerY += playerSpeed
                    
     # rgb
     screen.fill ((0, 0, 0))
     if playerX <= 0:
          playerX = 0
     if playerX >= 768:
          playerX = 768
     if playerY <= 0:
          playerY = 0
     if playerY >= 568:
          playerY = 568
     if enemyX <= 0:
          enemyX = 0
     if enemyX >= 768:
          enemyX = 768
     if enemyY <= 0:
          enemyY = 0
     if enemyY >= 568:
          enemyY = 568
     player(playerX, playerY)
     enemy (enemyX, enemyY)
     pygame.display.update()
