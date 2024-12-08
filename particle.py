import pygame
import random

class Particle:
    def __init__(self, x, y, velocity, color):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.color = color
        self.lifetime = 1.0  # Starts at 1, decreases to 0
        
    def update(self, dt):
        # Update position based on velocity
        self.x += self.velocity[0] * dt
        self.y += self.velocity[1] * dt
        # Decrease lifetime
        self.lifetime -= dt
        
    def draw(self, screen):
        pass