import pygame
from pygame.locals import *

pygame.init()
width,height = 640, 480
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Bebedilan')

running = True

sumbuY,sumbuX = 0,1
playerpos = [100,100] 

player = pygame.image.load("resources/images/dude.png")
rumput = pygame.image.load("resources/images/grass.png")
kastil = pygame.image.load("resources/images/castle.png")

keys = {
    "atas": False,
    "bawah": False,
    "kiri": False,
    "kanan": False
}

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

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys['atas'] = True
            elif event.key == K_a:
                keys['kiri'] = True
            elif event.key == K_s:
                keys['bawah'] = True
            elif event.key == K_d:
                keys['kanan'] = True
            
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys['atas'] = False
            elif event.key == K_a:
                keys['kiri'] = False
            elif event.key == K_s:
                keys['bawah'] = False
            elif event.key == K_d:
                keys['kanan'] = False

        if keys["atas"]:
            playerpos[sumbuX] -= 10
        elif keys["bawah"]:
            playerpos[sumbuX] += 10
        elif keys["kiri"]:
            playerpos[sumbuY] -= 10
        elif keys["kanan"]:
            playerpos[sumbuY] += 10