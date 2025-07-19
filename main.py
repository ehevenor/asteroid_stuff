import pygame
import sys
from constants import * 
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import *  
from shot import Shot

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group() 

    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)  
    Player.containers = (updatable, drawable) 
    Shot.containers = (updatable, drawable, shots)

    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField() 

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        dt = pygame.time.Clock().tick(60) / 1000.0  # Update dt with the time since the last frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0, 0, 0)) 
        
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for asteroid in asteroids:
            if player_one.collision(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    asteroid.split()
                    shot.kill() 

        pygame.display.flip()
    

if __name__ == "__main__":
    main()
