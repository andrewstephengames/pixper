import pygame
import random
import math

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
grassTile = pygame.image.load ("res/grasstile.png").convert()
tinyGrassTile = pygame.image.load ("res/tinyGrasstile.png").convert()

# player

playerImg = pygame.image.load("res/player-black.png")
enemyImg = pygame.image.load("res/enemy-black.png")
playerX = random.randint (0, width-32)
playerY = random.randint (0, height-32)
playerSpeed = 3

# enemy

enemyX = random.randint (0, width-32)
enemyY = random.randint (0, height-32)
enemySpeed = 1

# obstacles

#appleImg = pygame.image.load ("res/apple.png")
appleImg = []
#appleX = random.randint(0, width-32)
#appleY = random.randint (0, height-32)
appleX = []
appleY = []

appleNum = random.randint (0, 8)

for i in range (appleNum):
     appleImg.append (pygame.image.load("res/apple.png"))
     appleX.append(random.randint (0, width-32))
     appleY.append(random.randint (0, height-32))

# sounds

hurtSound = pygame.mixer.Sound ("res/sounds/oof.ogg")

# handle keys

keys = {'w': False,'a': False,'s': False,'d': False}
     
# entities

score = 0

def player(x, y):
     screen.blit(playerImg, (x, y))
def enemy(x, y):
     screen.blit(enemyImg, (x, y))
     global enemyX, enemyY, playerX, playerY, enemySpeed
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
     #screen.blit (grassImg, (0, 0))
     j = 0
     while j <= height:
               i = 0
               while i <= width:
                    screen.blit (grassTile, (i, j))
                    i += 256
               j += 256
     for i in range (2, appleNum):
          screen.blit (appleImg[i], (appleX[i], appleY[i]))
          if isCollision (playerX, playerY, appleX[i], appleY[i]):
               if appleImg[i] != tinyGrassTile:
                    score += 1
                    playerSpeed += 0.25
                    screen.blit (tinyGrassTile, (appleX[i], appleY[i]))
                    appleImg[i] = tinyGrassTile
     for event in pygame.event.get():
          # if screen gets resized adjust window size, entity speeds          
          if event.type == pygame.VIDEORESIZE:
               width = screen.get_width()
               height = screen.get_height()
               # FIXME
               playerSpeed = 1.5*(width/height)
               enemySpeed = 1.25*(width/height)
               #screen.blit (grassImg, (0, 0))
               #grassTile.blit(grassTile, (0, 0))
               j = 0
               while j <= height:
                    i = 0
                    while i <= width:
                         screen.blit (grassTile, (i, j))
                         i += 256
                    j += 256
                    firstFrame = True
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
     clock = pygame.time.Clock()
     clock.tick (75)
     pygame.display.update()
print ("Your final score was:", playerSpeed)
if score == 0:
     print ("You ate no apples.")
elif score == 1:
     print ("You ate", score, "apple.")
else: print ("You ate", score, "apples.")
