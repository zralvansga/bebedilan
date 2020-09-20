import pygame
from pygame.locals import *

pygame.init()
width,height = 640, 480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Bebedilan')

running = True

playerpos = [100,100]

player = pygame.image.load("resources/images/dude.png")
rumput = pygame.image.load("resources/images/grass.png")
kastil = pygame.image.load("resources/images/castle.png")

while(running):
    screen.fill(0)

    for x in range(int(width/rumput.get_width()+1)):
        for y in range(int(height/rumput.get_height()+1)):
            screen.blit(rumput, (x*100,y*100))

    screen.blit(kastil,(0,30))
    screen.blit(kastil,(0,135))
    screen.blit(kastil,(0,240))
    screen.blit(kastil,(0,345))
    
    screen.blit(player,playerpos)

    pygame.display.flip()
    # pygame.display.update() 
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
