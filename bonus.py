import pygame
import random
import math
from pygame import mixer

# initialize  the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load('imgs/bg.png')

# background sound
mixer.music.load('bg.wav')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Shinchan Hates Capsicum")
icon = pygame.image.load('imgs/shinchan.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('imgs/actionkamen.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

friendImg = []
friendX = []
friendY = []
friendX_change = []
friendY_change = []
num_of_friends = 2
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('imgs/capsicum.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 200))
    enemyX_change.append(3)
    enemyY_change.append(30)

for i in range(num_of_friends):
    friendImg.append(pygame.image.load("imgs/chocochips.png"))
    friendX.append(random.randint(0, 736))
    friendY.append(random.randint(50, 200))
    friendX_change.append(3)
    friendY_change.append(30)

# bullet
bulletImg = pygame.image.load('imgs/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  # ready means bullet is not seen on the screen

# score
score_value = 0
font = pygame.font.Font('comic.ttf', 32)
textX = 10
textY = 10

#gameover
over_font = pygame.font.Font('comic.ttf', 64)

#Exit Button


def display_text(x, y, text, colour):
    score = font.render(text, True, colour)
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))
    home_button()


def player(x, y):
    screen.blit(playerImg, (x, y))  # blit means to draw


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))  # blit means to draw

def friend(x,y,i):
    screen.blit(friendImg[i], (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # to fire bullet from the center of the spaceship aur slightly above


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True  # collision has occured
    else:
        return False
def friend_shoot(friendX, friendY, bulletX, bulletY):
    distance = math.sqrt((math.pow(friendX - bulletX, 2)) + (math.pow(friendY - bulletY, 2)))
    if distance < 27:
        return True  # collision has occured
    else:
        return False

#EXIT button
def exit_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (0,0,0), (648,23,119,54))
    if 775 > mouse[0] > 650 and 75 > mouse[1] > 25:
        pygame.draw.rect(screen, (220, 220, 220), (650, 25, 115, 50))
        if click[0] == 1:
            pygame.display.quit()
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(screen, (255, 255, 255), (650, 25, 115, 50))
    display_text(665, 26, "EXIT", (0, 0, 0))

def home_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, (0, 0, 0), (648, 223, 119, 54))
    if 775 > mouse[0] > 650 and 275 > mouse[1] > 225:
        pygame.draw.rect(screen, (220, 220, 220), (650, 225, 115, 50))
        if click[0] == 1:
            import start_screen
    else:
        pygame.draw.rect(screen, (255, 255, 255), (650, 225, 115, 50))
    display_text(660, 226, "HOME", (0, 0, 0))




# for holding the window
# game loop
run = True
while run:
    # RGB
    # background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # to close the window

        # if keystroke is pressed check whetherits right ot left
        if event.type == pygame.KEYDOWN:  # print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5  # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 5  # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('bibi.wav')
                    bullet_Sound.play()
                    bulletX = playerX  # current position if spaceship is given to bullet
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # print("keystroke has been released")

    playerX += playerX_change

    # adding boundaries so that spaceship n enemy doesn't go out of bound
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # since size of spaceship is 64x64 pixels therefore sub 64 by 800 i.e. 736
        playerX = 736


    # enemy movement
    for i in range(num_of_enemies):
        #gameover
        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:  # moves enemy down on hitting the boundary
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('expl6.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 200)

        enemy(enemyX[i], enemyY[i], i)



    for i in range(num_of_friends):
        if friendY[i]==440:
            score_value+=5

        friendX[i] += friendX_change[i]
        if friendX[i] <= 0:  # moves enemy down on hitting the boundary
            friendX_change[i] = 1
            friendY[i] += friendY_change[i]
        elif friendX[i] >= 736:
            friendX_change[i] = -1
            friendY[i] += friendY_change[i]
        friendshot = friend_shoot(friendX[i], friendY[i], bulletX, bulletY)
        if friendshot:
            game_over_text()
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            for j in range(num_of_friends):
                friendY[j] = 2000
            break

        friend(friendX[i], friendY[i], i)
    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    #Adding Butons
    exit_button()


    player(playerX, playerY)
    display_text(textX, textY, "SCORE:" + str(score_value) + "  EASY", (255,255,255))
    pygame.display.update()
