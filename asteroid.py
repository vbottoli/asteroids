import pygame
import random
from constants import *
from circleshape import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            v_1 = self.velocity.rotate(angle)
            v_2 = self.velocity.rotate(-angle)
            new_r = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position[0], self.position[1], new_r)
            asteroid_2 = Asteroid(self.position[0], self.position[1], new_r)
            asteroid_1.velocity = v_1 * 1.2
            asteroid_2.velocity = v_2 * 1.2

