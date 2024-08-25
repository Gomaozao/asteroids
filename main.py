import pygame
from player import Player
from constants import *

updatable_group = pygame.sprite.Group()
drawable_group = pygame.sprite.Group()
Player.containers = (updatable_group, drawable_group)

def main():
    pygame.init()
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
        
        screen.fill((0,0,1))

        for drawable in drawable_group:
            drawable.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()