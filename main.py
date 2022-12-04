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
icon = pygame.image.load("res/images/player.png")
pygame.display.set_icon (icon)

# background

#bgImg = pygame.image.load("res/background.jpg")

# tiles
grassImg = pygame.image.load ("res/images/grass.png")
grassTile = pygame.image.load ("res/images/grasstile.png")
tinyGrassTile = pygame.image.load ("res/images/tinyGrasstile.png")
bombTile = pygame.image.load ("res/images/bombtile.png")

# player

playerImg = pygame.image.load("res/images/player-black.png")
enemyImg = pygame.image.load("res/images/enemy-black.png")
playerX = random.randint (0, width-32)
playerY = random.randint (0, height-32)
playerSpeed = 3
playerHealth = 10
hitDelay = 20

# enemy

enemyX = random.randint (0, width-32)
enemyY = random.randint (0, height-32)
enemySpeed = 1

# obstacles

appleImg = []
appleX = []
appleY = []
appleNum = 0


grassTileImg = []
grassTileX = []
grassTileY = []
grassNum = 0

bombImg = []
bombX = []
bombY = []
bombNum = 0

treeImg = []
treeX = []
treeY = []
treeNum = 0

# fonts

healthFont = pygame.font.Font ("res/fonts/Emulogic.ttf", 20)
scoreFont = pygame.font.Font ("res/fonts/Emulogic.ttf", 20)
startFont = pygame.font.Font ("res/fonts/Emulogic.ttf", 40)
endFont = pygame.font.Font ("res/fonts/Emulogic.ttf", 70)

# sounds

hurtSound = pygame.mixer.Sound ("res/sounds/oof.ogg")
bombSound = pygame.mixer.Sound ("res/sounds/boom.ogg")
eatSound = pygame.mixer.Sound ("res/sounds/eat.ogg")
hurtSound.set_volume(0.25)
bombSound.set_volume(0.25)
eatSound.set_volume(0.25)

# music

mainMusic = pygame.mixer.music.load("res/music/mainmusic.ogg")

# play music indefinitely
pygame.mixer.music.play (-1)

# handle keys

keys = {'w': False,'a': False,'s': False,'d': False}
     

score = 0

# entities

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
     
def isCollision (x1, y1, x2, y2, collide):
     distance = math.sqrt(math.pow(x2-x1, 2) + math.pow (y2-y1, 2))
     return distance < collide

def generateApple (init):
     global appleImg, appleX, appleY, appleNum, tinyGrassTile
     global playerX, playerY, playerSpeed, score, width, height, playerHealth
     if init:
          appleNum = random.randint (16, 64)
          for i in range (appleNum):
               appleImg.append (pygame.image.load("res/images/apple.png"))
               appleX.append(random.randint (0, width-32))
               appleY.append(random.randint (0, height-32))
     else:
          for i in range (appleNum):
               screen.blit (appleImg[i], (appleX[i], appleY[i]))
               if isCollision (playerX, playerY, appleX[i], appleY[i], 10):
                    if appleImg[i] != tinyGrassTile:
                         eatSound.play()
                         eatSound.set_volume(0.1)
                         score += 1
                         playerSpeed += 0.25
                         screen.blit (tinyGrassTile, (appleX[i], appleY[i]))
                         appleImg[i] = tinyGrassTile
                         playerHealth += 1

def generateGrass (init):
     global grassNum, grassTileImg, grassTileX, grassTileY, width, height
     if init:
          grassNum = random.randint (32, 256)
          for i in range (grassNum):
               grassTileImg.append (pygame.image.load ("res/images/tinyGrasstile.png"))
               grassTileX.append (random.randint (0, width-32))
               grassTileY.append (random.randint (0, height-32))
     else:
          for i in range (grassNum):
               screen.blit (grassTileImg[i], (grassTileX[i], grassTileY[i]))
def generateBomb (init):
     global bombNum, bombImg, bombX, bombY, width, height, playerHealth
     global enemyX, enemyY, playerX, playerY, playerSpeed, enemySpeed
     global bombTile
     if init:
          bombNum = random.randint (32, 64)
          for i in range (bombNum):
               bombImg.append (pygame.image.load ("res/images/bomb.png"))
               bombX.append (random.randint (0, width-32))
               bombY.append (random.randint (0, height-32))
     else:
          for i in range (bombNum):
               screen.blit (bombImg[i], (bombX[i], bombY[i]))
               if isCollision (playerX, playerY, bombX[i], bombY[i], 15):
                    if bombImg[i] != bombTile:
                         playerHealth -= 10
                         playerSpeed -= 0.5
                         screen.blit (bombTile, (bombX[i], bombY[i]))
                         bombImg[i] = bombTile
                         bombSound.play()
                         bombSound.set_volume(0.1)
                         hurtSound.play()
                    else:
                         playerX -= 32
                         playerY -= 32
               if isCollision (enemyX, enemyY, bombX[i], bombY[i], 15):
                    if bombImg[i] != bombTile:
                         enemySpeed += 0.5
                         screen.blit (bombTile, (bombX[i], bombY[i]))
                         bombImg[i] = bombTile
                         bombSound.play()
                         bombSound.set_volume(0.1)
                    else:
                         if playerX == bombX[i] and playerY == bombY[i]:
                              playerX -= 1
                              playerY -= 1

def generateTree (init):
     global treeImg, treeX, treeY, treeNum, playerX, playerY
     if init:
          treeNum = random.randint (16, 64)
          for i in range (treeNum):
               treeImg.append (pygame.image.load ("res/images/tree.png"))
               treeX.append (random.randint (0, width-32))
               treeY.append (random.randint (0, height-32))
     else:
          for i in range (treeNum):
               screen.blit (treeImg[i], (treeX[i], treeY[i]))
          
     

generateBomb (True)
generateApple (True)
generateGrass (True)
generateTree(True)

iterationNum = 0


# gameloop
running = True
while running:
     iterationNum += 1
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
     generateApple(False)
     generateGrass(False)
     generateBomb (False)
     generateTree(False)
     for event in pygame.event.get():
          # if screen gets resized adjust window size, entity speeds          
          if event.type == pygame.VIDEORESIZE:
               newwidth = screen.get_width()
               newheight = screen.get_height()
               #playerSpeed = 2.5*(newwidth/newheight)
               #enemySpeed = 1.5*(newwidth/newheight)
               width = newwidth
               height = newheight
               #appleNum = random.randint ( (int) (width/height)*2, (int) (width/height)*32)
               #grassNum = random.randint ( (int) (width/height)*8, (int) (width/height)*64)
               generateApple(True)
               generateGrass(True)
               generateTree(True)
               generateBomb(True)
               generateApple(False)
               generateGrass(False)
               generateBomb (False)
               generateTree(False)
               
               #screen.blit (grassImg, (0, 0))
               #grassTile.blit(grassTile, (0, 0))
               j = 0
               while j <= height:
                    i = 0
                    while i <= width:
                         screen.blit (grassTile, (i, j))
                         i += 256
                    j += 256
               if iterationNum < 20:
                    screen.blit (startFont.render("Gotta eat em all!", True, (0, 0, 0)), (width/8, height/2))
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

     
     collision = isCollision (playerX, playerY, enemyX, enemyY, 5)
     if collision and hitDelay == 0:
          hurtSound.play()
          hurtSound.set_volume(0.1)
          playerHealth -= 3
          #playerSpeed -= 0.25
          hitDelay = 20
     elif collision and hitDelay != 0:
          hitDelay -= 1
     if playerHealth <= 0:
          playerHealth = 0
          screen.blit (endFont.render ("Game Over!", True, (163.6, 162.5, 162.5)), (width/10, height/2.5))
          screen.blit (endFont.render ("Score:" + str(score), True, (0, 0, 255)), (width/5, height/2))
          iterationNum = 0
     elif score == appleNum-1:
          screen.blit (endFont.render ("You Won!", True, (223.8, 225.7, 12.1)), (width/5, height/2.5))
          screen.blit (endFont.render ("Score:" + str(score), True, (0, 0, 255)), (width/5, height/2))
          iterationNum = 0
     
     player(playerX, playerY)
     enemy (enemyX, enemyY)
     screen.blit (healthFont.render("Health:" + str(playerHealth), True, (255, 0, 0)), (0, 0))
     screen.blit (scoreFont.render("Score:" + str(score), True, (0, 0, 255)), (0, 25))
     if iterationNum < 80 and iterationNum > 0:
          screen.blit (startFont.render("Gotta eat em all!", True, (0, 0, 0)), (width/8, height/2.5))
     clock = pygame.time.Clock()
     clock.tick (75)
     pygame.display.update()
     if iterationNum == 0:
          pygame.time.wait(5000)
          running = False
if score == 0:
     print ("You ate no apples.")
elif score == 1:
     print ("You ate", score, "apple.")
else: print ("You ate", score, "apples.")
