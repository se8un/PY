import pygame

WIDTH, HEIGHT = 1200, 800
fps = 60

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #update screen
    pygame.display.flip()
    clock.tick(fps)


