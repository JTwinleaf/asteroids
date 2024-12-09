import pygame

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, pos):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        self.pos = pos
        self.update_text()
    
    def update_text(self):
        self.image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=self.pos)
    
    def update(self, score):
        if score != self.score:
            self.score = score
            self.update_text()
