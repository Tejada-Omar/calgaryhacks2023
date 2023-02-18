import pygame


class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image


class Pet(pygame.sprite.Sprite):
    def __init__(self,spriteSheet, health = 100, hunger = 100, fitness = 100, energy = 100):
        super().__init__()
        self.sprite = SpriteSheet(spriteSheet)
        # self.rect = self.sprite.get_Rect()
        # self.rect.center = (x, y)
        self.health = health
        self.hunger = hunger
        self.fitness = fitness
        self.energy = energy

    def move(self, x=0, y=1):
        self.rect.move_ip(x,y)

    def draw(self, _surface, frame , width, height, location, scale = 1, colour = (255, 255, 255)):
        
        
        _surface.blit(self.sprite.get_image(frame, width, height, scale, colour), location)

    def getHunger(self):
        return self.hunger

    def setHunger(self, amount):
        self.hunger = min(100, amount)

    def getFitness(self):
        return self.hunger

    def setFitness(self, amount):
        self.fitness = min(100, amount)

    def getEnergy(self):
        return self.hunger

    def setEnergy(self, amount):
        self.energy = min(100, amount)
