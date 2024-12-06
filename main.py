# this allows us to use code from
# the open-source pygame library
# throughout this file
# owo what's this?
import pygame
from constants import *
from player import *
from shot import *
from asteroid import *
from asteroidfield import *
from circleshape import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    score = 0
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for entity in updateable:
            entity.update(dt)

        for asteroid in asteroids:
            if asteroid.collide_check(player) == True:
                print("Game Over!")
                print(f"You scored: {score} points!")
                if score >= 100000:
                    print("You're crazy good!")
                return pygame.QUIT
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collide_check(asteroid) == True:
                    shot.kill()
                    asteroid.split()
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 100
                    else:
                        score += 10

        screen.fill("black")

        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
