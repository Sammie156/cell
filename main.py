import random
import pygame

from agents.basic import BasicModel
from components.food import Food

COLOR = ["blue", "purple", "green"]

pygame.init()
screen = pygame.display.set_mode((1280,720)) # For now this is the world limit
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(-200, 0)

model =  BasicModel()
foods: list[Food] = []

for i in range(5):
    food_w = random.randint(0, 1280)
    food_h = random.randint(0, 720)
    food_pos = pygame.Vector2(food_w, food_h)
    food_size = random.randint(10, 20)
    food_color = random.choice(COLOR)

    food = Food(food_color, food_pos, food_size)
    foods.append(food)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    screen.fill("black")

    # Render here
    model.draw_agent(screen)

    for food in foods:
        food.draw_food(screen)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
