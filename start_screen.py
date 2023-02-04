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

def buttons():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 330 > mouse[0] > 30 and 350> mouse[1] >250:
        background = pygame.image.load('imgs/easy.png')
        if click[0] == 1:
            import lvl_easy
    elif 770 > mouse[0] > 470 and 350 > mouse[1] > 250:
        background = pygame.image.load('imgs/difficult.png')
        if click[0] == 1:
            import lvl_diff
    elif 330 > mouse[0] > 30 and 500 > mouse[1] > 400:
        background = pygame.image.load('imgs/HTP.png')
        if click[0] == 1:
            import HTP
    elif 770 > mouse[0] > 470 and 500 > mouse[1] > 400:
        background = pygame.image.load('imgs/bonus.png')
        if click[0] == 1:
            import bonus_inst
    else:
        background = pygame.image.load('imgs/intro.png')
    return background


def exit_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 180 > mouse[0] > 30 and 200 > mouse[1] > 125:
        exitbutton = pygame.image.load('imgs/exit2.png')
        if click[0] == 1:
            pygame.display.quit()
            pygame.quit()
            quit()
    else:
        exitbutton = pygame.image.load('imgs/exit1.png')
    return  exitbutton

while True:
    screen.blit(buttons(), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # to close the window
    screen.blit(exit_button(),(30,125))
    pygame.display.update()
