import random
import pygame

from agents.worm import Worm

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

points: list[pygame.Vector2] = []

worm = Worm()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            points.append(pygame.Vector2(pygame.mouse.get_pos()))

    # I like killing the window with escape...
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_SPACE]:
        points.clear()

    screen.fill("black")


    worm.draw_worm(screen)
    worm.worm_state(points, dt)
    for point in points:
        pygame.draw.circle(screen, "red", point, 5)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
