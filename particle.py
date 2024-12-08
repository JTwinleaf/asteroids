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
        import math

def draw(self, screen):
    cx, cy = int(self.x), int(self.y)
    main_size = 8  # made slightly longer
    branch_size = 3
    branch_offset = 0.6  # This means branches start 60% along the main arm
    
    # For each main arm
    for angle in range(0, 360, 60):
        rad = math.radians(angle)
        
        # Calculate end point of main arm
        end_x = cx + main_size * math.cos(rad)
        end_y = cy + main_size * math.sin(rad)
        
        # Draw main arm
        pygame.draw.line(screen, self.color, (cx, cy), (end_x, end_y))
        
        # Calculate branch starting point (part way along main arm)
        branch_start_x = cx + (main_size * branch_offset) * math.cos(rad)
        branch_start_y = cy + (main_size * branch_offset) * math.sin(rad)
        
        # Add branches (30 degrees from main arm)
        branch_rad1 = rad + math.radians(30)
        branch_rad2 = rad - math.radians(30)
        
        # Calculate branch endpoints from new starting point
        branch1_x = branch_start_x + branch_size * math.cos(branch_rad1)
        branch1_y = branch_start_y + branch_size * math.sin(branch_rad1)
        branch2_x = branch_start_x + branch_size * math.cos(branch_rad2)
        branch2_y = branch_start_y + branch_size * math.sin(branch_rad2)
        
        # Draw branches from offset point
        pygame.draw.line(screen, self.color, 
                        (branch_start_x, branch_start_y), 
                        (branch1_x, branch1_y))
        pygame.draw.line(screen, self.color, 
                        (branch_start_x, branch_start_y), 
                        (branch2_x, branch2_y))