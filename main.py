import pygame



class Pet():
    def __init__(self, health, food, exercise, energy):
        self.health = health
        self.food = food
        self.exercise = exercise
        self.energy = energy

    def feed(self):