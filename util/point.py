from __future__ import annotations
import pygame


class Point:
    def __init__(self, radius: float, color: str) -> None:
        self.position: pygame.Vector2 = pygame.Vector2(100, 100)
        self.velocity: pygame.Vector2 = pygame.Vector2()
        self.radius: float = radius
        self.color: str = color

    def constraint_distance(self, anchor: Point):
        diff = self.position - anchor.position

        target_distance = self.radius + anchor.radius

        if diff.length_squared() == 0:
            diff = pygame.Vector2(1, 0)
        else:
            diff = diff.normalize()

        self.position = anchor.position + diff * target_distance

    def draw_point(self, screen: pygame.Surface, anchor: Point):
        self.constraint_distance(anchor)
        pygame.draw.circle(screen, self.color, self.position, self.radius)
