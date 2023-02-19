import pygame

class Button():
    def __init__(self, colour, x, y, width, height, font, text='', textSize=32):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(font, textSize)
        self.text = text

    def draw(self, screen, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(screen, self.colour, (self.x,self.y,self.width,self.height),0)

        if self.text != '':

            text = self.font.render(self.text, True, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def getMouseClick(self, pos):
        return self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y
