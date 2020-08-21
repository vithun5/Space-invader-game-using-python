import pygame
import os
import random
import math
from pygame import mixer
pygame.init()





#Display
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Space Invaders')

icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)



#BackGround

background = pygame.image.load('background_1.png')
screen.blit(background,(0,0)) 


#Player

player_1 = pygame.image.load('rocket.png')
playerX = 365
playerY = 480
playerX_change = 0


#Bullet

bullet_1 = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 3
bulletY_change = 10
bullet_state = 'ready'


#Enemies

enemy_1 = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 9

for x in range(number_of_enemies):
    enemy_1.append( pygame.image.load('Enemies.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,100))
    enemyX_change.append(1)
    enemyY_change.append(40)


#score
score_1 = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 32)
font_1 = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x,y):
    score = font.render('Score: {0}'.format(score_1),True,(255,0,0))
    screen.blit(score,(x,y))
def game_over(x,y):
    gameover = font_1.render('GAME OVER',True,(255,0,0))
    screen.blit(gameover,(200,250))
# required functions
def player(x,y):
    screen.blit(player_1,(x,y))
def enemy(x,y,i):
    screen.blit(enemy_1[i],(x,y))
def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_1,(x+16,y+10))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((bulletX-enemyX)**2+(bulletY-enemyY)**2)
    if distance <= 25:
        return True
    else:
        return False
    

running = True
while running:
    screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = 6
                print('Left Arrow is pressed.')
            if event.key == pygame.K_RIGHT:
                playerX_change = -6
                print('Right Arrow is pressed')
            if event.key == pygame.K_SPACE:
                print('Space Bar is pressed')
                if bullet_state is 'ready':
                    bulletX = playerX
                    bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                playerX_change = 0
                print('Left arrow is released')
            if event.key == pygame.K_RIGHT:
                playerX_change = 0
                print('Right arrow is realesed')
            if event.key == pygame.K_SPACE:
                print('Space Bar is released')
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    #PlayerssssS!
    playerX -= playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >736:
        playerX = 736
    #Game Over
    for x in range(number_of_enemies):
        if enemyY[x] > 480:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over(200,250)

            break
    #Collision
    for x in range(number_of_enemies):
        collision = isCollision(enemyX[x],enemyY[x],bulletX,bulletY)
        if collision is True:
            score_1 += 1
            enemyX[x] = random.randint(0,736)
            enemyY[x] = random.randint(50,150)
    #Enemies!!!!
    for x in range(number_of_enemies):
        enemyX[x] += enemyX_change[x]
        if enemyX[x] <= 0 :
            enemyX_change[x] = 1
            enemyY[x] += enemyY_change[x]
        if enemyX[x] >= 736:
            enemyX_change[x] = -1
            enemyY[x] += enemyY_change[x]
        enemy(enemyX[x],enemyY[x],x)
    #Bullet
    if bullet_state is 'fire':
        bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bullet_state = 'ready'
        bulletY = 480



    show_score(textX,textY)
    player(playerX,playerY)
    
    



    pygame.display.update()
