import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS, FESTIVE_COLORS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.outline, self.color = random.choice(list(FESTIVE_COLORS.items()))

    def draw(self, screen):
        cap_width = 25
        cap_height = 20
        cap_x = self.position.x - (cap_width/2)
        cap_y = self.position.y - self.radius - cap_height
        pygame.draw.circle(screen, self.color, self.position, self.radius)
        pygame.draw.circle(screen, self.outline, self.position, self.radius, 2)
        pygame.draw.rect(screen, "gold",(cap_x, cap_y, cap_width, cap_width))
        pygame.draw.rect(screen, "brown",(cap_x, cap_y, cap_width, cap_width), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
        else:
            self.kill()
            random_angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position, self.position, new_radius)
            asteroid_1.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid_2 = Asteroid(self.position, self.position, new_radius)
            asteroid_2.velocity = self.velocity.rotate(-random_angle) * 1.2