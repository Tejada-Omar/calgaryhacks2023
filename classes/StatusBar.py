import pygame
from classes.Pet import SpriteSheet

class StatusBar(pygame.sprite.Sprite):

    def __init__(self, spriteSheet, color = (255,0,0), position = (0,0),
                 percent=1, width = 200, height = 20,
                 font="assets/fonts/Mynerve-Regular.ttf", text = "",):
        super().__init__()
        self.sprite = spriteSheet
        self.percent = percent
        self.width = width
        self.height = height
        self.color = color
        self.position = position
        self.text = text
        textSize = self.height
        self.font = pygame.font.Font(font, textSize)

    def setPercent(self, percent):
        self.percent = percent

    # def draw(self, _surface, frame , width, height, location, scale = 1, colour = (0, 0, 0)):
	# def get_image(self, frame, width, height, scale, colour):
    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,255), (self.position, (self.width, self.height)))
        pygame.draw.rect(surface, self.color, (self.position, (self.width*self.percent, self.height)))

        if(self.text != ""):
            text = self.font.render(self.text, 1, (0,0,0))
            surface.blit(text, self.position)

        surface.blit(self.sprite.get_image(1, self.height, self.height, 1, (0, 0, 0)), self.position)
