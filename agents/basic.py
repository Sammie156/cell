"""
A basic agent that simply moves around, and stays in the screen.
"""

import pygame

class BasicModel:
    def __init__(self) -> None:
        self.speed: float = 20.0
        self.color: str = "red"  # dummy color
        self.radius: float = 40.0

    def draw_agent(self, screen: pygame.Surface) -> None:
        width = screen.get_width() / 2
        height = screen.get_height() / 2
        agent_pos = pygame.Vector2(width, height)

        pygame.draw.circle(screen, self.color, agent_pos, self.radius)
