import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)     
        
    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt