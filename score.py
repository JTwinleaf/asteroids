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
        self.game_over = False
    
    def update_text(self):
        self.image = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=self.pos)
    
    def update(self, score):
        if score != self.score:
            self.score = score
            self.update_text()
        
        if self.game_over:
            if self.target_pos is None:
                screen_rect = pygame.display.get_surface().get_rect()
                self.target_pos = (screen_rect.centerx - self.rect.width // 2, screen_rect.centery)
            

    def draw(self, screen):
        screen.blit(self.image, self.rect)