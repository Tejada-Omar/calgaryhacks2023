import pygame
import os
from SpriteSheet import SpriteSheet

class Food(pygame.sprite.Sprite):
    def __init__(self, spriteSheet, name, healthRating, hungerRating):
        super().__init__()
        self.sprite = SpriteSheet(spriteSheet)
        self.healthRating = healthRating
        self.hungerRating = hungerRating
        self.name = name

        if type(self) == Food:
            raise TypeError("<Food> must be subclasses")

    def move(self, x = 0, y = 1):
        self.rect.move_ip(x, y)

    def draw(self, _surface, frame , width, height, location, scale = 1, colour = (255, 255, 255)):
        _surface.blit(self.sprite.get_image(frame, width, height, scale, colour), location)

    def getSprite(self):
        return self.sprite

    def getHealthRating(self):
        return self.healthRating

    def getHungerRating(self):
        return self.hungerRating

    def getName(self):
        return self.name

class Apple(Food):
    def __init__(self):
        folder = "assets/pets"
        spriteSheet = pygame.image.load(os.path.join(folder,
                                                     "catBlack.png",)).convert_alpha()
        self.name = "Apple"
        self.healthRating = 5
        self.hungerRating = 5
        super().__init__(spriteSheet, self.name, self.healthRating, self.hungerRating)
