import pygame
from pygame import mixer

# initialize  the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background sound
mixer.music.load('bg.wav')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Shinchan Hates Capsicum")
icon = pygame.image.load('imgs/shinchan.png')
pygame.display.set_icon(icon)



def btn():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 250 > mouse[0] > 100 and 575 > mouse[1] > 500:
        background = pygame.image.load('imgs/bonus_inst1.png')
        if click[0] == 1:
            import bonus
    else:
        background = pygame.image.load('imgs/bonus_inst.png')
    return background

while True:
    screen.blit(btn(), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # to close the window
    pygame.display.update()
