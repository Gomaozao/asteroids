import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()

    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()

    Player.containers = (updatable_group, drawable_group)
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable in updatable_group:
            updatable.update(dt)
        
        for asteroid in asteroids_group:
            if asteroid.is_collided(player1) == True:
                print ("Game over!")
                sys.exit()

        screen.fill((0,0,1))

        for drawable in drawable_group:
            drawable.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()