"""
Food for the agents.
Right now, just basic food.
"""

import pygame


class Food:
    def __init__(self, color: str, position: pygame.Vector2, size: float) -> None:
        self.color: str = color
        self.position: pygame.Vector2 = position
        self.size: float = size

    def draw_food(self, screen: pygame.Surface):
        pygame.draw.circle(screen, self.color, self.position, self.size)
