"""
A basic organism, with multiple parts.

CURRENT IMPLEMENTATION:
Understanding distance constraints, 4 circles following each other, which makes it look like a WORM
"""

import pygame

default_val: pygame.Vector2 = pygame.Vector2(0, 0)
SEGMENTS: int = 5

# basically holds the center of all the parts of the worm

class Worm:
    def __init__(self, position, velocity=default_val, age=1) -> None:
        self.position: pygame.Vector2 = position
        self.velocity: pygame.Vector2 = velocity
        self.age: int = age
