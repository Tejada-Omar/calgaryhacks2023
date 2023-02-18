import pygame

class Pet(pygame.sprite.Sprite):
    def __init__(self,spriteSheet, x=0, y=0, health = 100, hunger = 100, fitness = 100, energy = 100):
        super().__init__()
        self.sprite = pygame.image.load(spriteSheet).convert_alpha()
        # self.rect = self.sprite.get_Rect()
        # self.rect.center = (x, y)
        self.health = health
        self.hunger = hunger
        self.fitness = fitness
        self.energy = energy

    def move(self, x=0, y=1):
        self.rect.move_ip(x,y)

    def draw(self, _surface, frame , width, height, scale = 1, colorkey = None):
        img = pygame.surface.Surface((width, height))
        img.blit(self.sprite, (0,0), (frame * width, 0, width, height))
        img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        if colorkey  !=  None:
            if colorkey == -1:
                colorkey = img.get_at((0,0))
            img.set_colorkey(colorkey, pygame.RLEACCEL)
        _surface.blit(_surface, (0,0))

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
