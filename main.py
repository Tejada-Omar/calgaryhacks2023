import sys, pygame
import Pet
import Background
import time
import os
pygame.init()

size = width, height = 800, 600

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
        

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen.blit(Background.sprite, Background.rect)
        #draw button in the middle of the screen
        screen.fill((157, 141, 128)) 
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
        if hasStarted:
            if firstPlay:
                ## pick pet
                ## look through assets/pets
                folder = "assets/pets"
                
                for filename in os.listdir(folder):
                    if filename.endswith(".png"):
                        surface = pygame.image.load(os.path.join(folder, filename)).convert_alpha()
                        pets.append(Pet.Pet(surface))

                        
                        print(filename)

                #draw pet selection screen
                for i in range(len(pets)):
                    pets[i].draw(screen, 0, 25, 25, (i*32, 0))
                    print(i)
                
                #halt program until user selects pet
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        for i in range(len(pets)):
                            if pos[0] < (i+1)*25 and pos[0] > i*25:
                                print("selected pet: " + str(i))
                                name = input("Enter a name for your pet: ")
                                pets[i].setName(name)
                                print(pets[i].name)
                                firstPlay = False
                                break
                    pygame.display.flip()
                

                    

                ## name pet 


            
            

            
        





        pygame.display.flip()




main()
