import random
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

COLORS = ["blue", "blue1", "blue2", "blue3", "blue4"]


def constraint_distance(point: pygame.Vector2, anchor: pygame.Vector2, distance: float):
    diff = point - anchor
    # Prevent crash if point and anchor are at the exact same spot
    if diff.length() == 0:
        return anchor + pygame.Vector2(distance, 0)
    return (diff.normalize() * distance) + anchor


def draw_anchor(screen: pygame.Surface, coordinate):
    pygame.draw.circle(screen, "white", coordinate, anchor_radius)
    # pygame.draw.circle(screen, "blue", coordinate, anchor_dist, width=2)


def draw_point(
    screen: pygame.Surface,
    anchor,
    point: pygame.Vector2,
    dist: float,
    color: str,
    radius: float,
):
    constrained_pos = constraint_distance(point, anchor, dist + 2)
    pygame.draw.circle(screen, color, constrained_pos, radius)
    return constrained_pos


anchor = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
anchor_radius: int = 20
anchor_dist: int = 10 + anchor_radius

point = pygame.Vector2(100, 100)
point_radius = 17
point_col = random.choice(COLORS)
COLORS.remove(point_col)

point2 = pygame.Vector2()
point2_radius = 15
point2_col = random.choice(COLORS)
COLORS.remove(point2_col)


point3 = pygame.Vector2()
point3_radius = 13
point3_col = random.choice(COLORS)
COLORS.remove(point3_col)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    anchor = pygame.mouse.get_pos()

    draw_anchor(screen, pygame.mouse.get_pos())
    point = draw_point(screen, anchor, point, anchor_dist, point_col, point_radius)
    point2 = draw_point(screen, point, point2, point_radius, point2_col, point2_radius)
    point3 = draw_point(screen, point2, point3, point2_radius, point3_col, point3_radius)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()
