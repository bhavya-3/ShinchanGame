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
background = pygame.image.load('imgs/HowToPlay.png')


def exit_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 750 > mouse[0] > 600 and 500 > mouse[1] > 425:
        exitbutton = pygame.image.load('imgs/exit2.png')
        if click[0] == 1:
            pygame.display.quit()
            pygame.quit()
            quit()
    else:
        exitbutton = pygame.image.load('imgs/exit1.png')
    return  exitbutton

def home_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 750 > mouse[0] > 600 and 375 > mouse[1] > 300:
        homebutton = pygame.image.load('imgs/home1.png')
        if click[0] == 1:
            import start_screen
    else:
        homebutton = pygame.image.load('imgs/home2.png')
    return  homebutton

while True:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False  # to close the window
    screen.blit(exit_button(),(600,425))
    screen.blit(home_button(), (600, 300))
    pygame.display.update()
