import pygame
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__x_pos = x
        self.__y_pos = y

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.__x_pos, self.__y_pos), self.radius, 2)

    def update(self, dt):
        self.velocity += dt
