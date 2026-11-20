import random
import pygame

from agents.worm import Worm

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()
running = True
dt = 0

worm = Worm()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # I like killing the window with escape...
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    screen.fill("black")

    worm.draw_worm(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
