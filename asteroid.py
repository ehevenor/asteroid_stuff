import pygame
import random
from circleshape import CircleShape
from constants import * 
from player import Player 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, surface):
        super().draw(surface)
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
      
        random_angle = random.uniform(20, 50)
            
        new_radius = self.radius - ASTEROID_MIN_RADIUS
            
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2    
            
        