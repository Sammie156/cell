import math
import pygame

from util.point import Point

RADII: list[int] = [10, 8, 6, 4]


class Worm:
    def __init__(self) -> None:
        self.points: list[Point] = []
        self.amplitude: int = 2
        self.speed: float = 0.002 # TODO: Maybe the speed depends on the activity or state of the worm
        self.base_radii: list[int] = RADII.copy()
        self.velocity: pygame.Vector2 = pygame.Vector2(1, 1)

        for i, radius in enumerate(RADII):
            point: Point = Point(radius, f"cyan{abs(i-4)}")
            point.position = pygame.Vector2(100 - i * 20, 100)
            self.points.append(point)

    # FIXME: Implement this when there is nothing for the worm to eat or do
    def wander_worm(self) -> None:
        pass
    
    # TODO: Please make the movement look better
    def move_worm(self, target: pygame.Vector2, dt: float) -> bool:
        head  = self.points[0].position
        diff = target - head

        if diff.length() == 0 or head.distance_to(target) <= 5:
            return True
        else:
            self.points[0].position.move_towards_ip(target, 2)
            return False

    def worm_state(self, points: list[pygame.Vector2], dt: float) -> None:
        if len(points) == 0:
            self.wander_worm()
        else:
            # FIXME: Instead of moving the first element of the array, move to the closest one
            if self.move_worm(points[0], dt):
                points.pop(0)
                print(points)

    def draw_worm(self, screen: pygame.Surface) -> None:
        # We need to draw the head at the mouse position
        pygame.draw.circle(
            screen, self.points[0].color, self.points[0].position, self.points[0].radius
        )
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
