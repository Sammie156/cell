import math
import pygame

from util.point import Point

RADII: list[int] = [24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]


class Worm:
    def __init__(self) -> None:
        self.points: list[Point] = []
        self.amplitude = 2
        self.speed = 0.002 # TODO: Maybe the speed depends on the activity or state of the worm
        self.base_radii = RADII.copy()

        for i, radius in enumerate(RADII):
            point: Point = Point(radius, f"gray{i+67}")
            point.position = pygame.Vector2(100 - i * 20, 100)
            self.points.append(point)

    def draw_worm(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        # We need to draw the head at the mouse position
        pygame.draw.circle(
            screen, self.points[0].color, mouse_pos, self.points[0].radius
        )
        self.points[0].position = pygame.Vector2(
            mouse_pos
        )  # forgot this... now it works
        time_ms = pygame.time.get_ticks()
        phase = time_ms * self.speed - 0 * 0.5
        self.points[0].radius = self.base_radii[0] + self.amplitude * math.sin(phase)

        for i in range(1, len(self.points)):
            current_point = self.points[i]
            anchor_point = self.points[i - 1]
            time_ms = pygame.time.get_ticks()
            phase = time_ms * self.speed - i * 0.5
            current_point.radius = self.base_radii[i] + self.amplitude * math.sin(phase)
            current_point.draw_point(screen, anchor_point)
