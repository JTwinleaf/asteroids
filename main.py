# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updateable:
            entity.update(dt)

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
