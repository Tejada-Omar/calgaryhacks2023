import sys, pygame
import Pet
import Background
pygame.init()

size = width, height = 400, 400

screen = pygame.display.set_mode(size)

cat = pygame.image.load("assets/pets/catOrange.png").convert_alpha()
background = Background.Background("assets/background.png", (0,0))

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image


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
    <<<<<<< HEAD
            text = self.font.render(self.text, 1, (0,0,0))
=======
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, True, (0,0,0))
>>>>>>> a6b0a715f0b5e1bac3863c422dc96c13b32f5665
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def getMouseClick(self, pos):
        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True

        return False

def main():
    FPS = 60
    clock = pygame.time.Clock()

    hasStarted = False
    startButton = Button((96, 87, 95), 150, 175, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Start')
    while True:
        frame = SpriteSheet(cat).get_image(0, 25, 25, 2, (0,0,0))

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

<<<<<<< HEAD

        # main game loop
        if hasStarted:
            
        
=======
>>>>>>> a6b0a715f0b5e1bac3863c422dc96c13b32f5665





        pygame.display.flip()




main()
