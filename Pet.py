import pygame

class Pet(pygame.sprite.Sprite):
    def __init__(self, health = 100, hunger = 100, fitness = 100, energy = 100):
        super().__init__()
        
        self.health = health
        self.hunger = hunger
        self.fitness = fitness
        self.energy = energy

    def setHunger(self, amount):
        self.hunger = min(100, amount)
        
    def setFitness(self, amount):
        self.fitness = min(100, amount)
    
    def setEnergy(self, amount):
        self.energy = min(100, amount)