import sys, pygame
import classes.Pet as Pet
import Background
import time
import os
pygame.init()

size = width, height = 400, 400

screen = pygame.display.set_mode(size)

background = Background.Background("assets/background.png", (0,0))


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

            text = self.font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def getMouseClick(self, pos):
        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True

        return False

def main():
    FPS = 60
    clock = pygame.time.Clock()
    currentTime = time.time()
    firstPlay = True
    hasStarted = False
    startButton = Button((96, 87, 95), 150, 175, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Start')
    pets = []
    while True:
        frame = SpriteSheet(cat).get_image(0, 25, 25, 2, (0,0,0))

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen.blit(Background.sprite, Background.rect)
        #draw button in the middle of the screen
        
        screen.fill((157, 141, 128)) 
        pygame.draw.rect(screen, (255,0,0), (0,0,400,400))
        if not hasStarted:
            startButton.draw(screen)

        #check if the mouse is clicked
        if not hasStarted:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if startButton.getMouseClick(pos):
                    print("Clicked")
                    hasStarted = True
                    #destroy button
                    startButton = None

                


        # main game loop
<<<<<<< HEAD
        #if hasStarted:
=======
        if hasStarted:
            if firstPlay:
                ## pick pet
                ## look through assets/pets
                folder = "assets/pets"
                for filename in os.listdir(folder):
                    if filename.endswith(".png"):
                        pets.append(Pet.Pet(filename, (0,0)))

                    

                ## name pet 


            
            

>>>>>>> 9b663c1602d4bc530b9da4f0f93746d47203c90c
            
        





        #pygame.display.flip()




main()
