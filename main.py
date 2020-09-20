import pygame
from pygame.locals import *

pygame.init()
lebar,tinggi = 640, 480
screen = pygame.display.set_mode((lebar,tinggi))

running = True

playerpos = [100,100]

player = pygame.image.load("resources/images/dude.png")

while(running):
    screen.fill(0)
    screen.blit(player,playerpos)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
