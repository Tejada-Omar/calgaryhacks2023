import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, sprite, position):
        super().__init__()
        self.sprite = pygame.image.load(sprite)
        # self.rect = self.sprite.get_Rect()
        # self.rect.left, self.rect.top = position
