import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

black = (0,0,0)
white = (255,255,255)

dt = 0
clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Flappy Gachi')


stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    


    pygame.display.update()
    dt = clock.tick(FPS) / 1000


pygame.quit()
quit()