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
    def __init__(self, colour, x, y, width, height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(screen, self.colour, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def getMouseClick(self, pos):
        if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
            return True

        return False

def main():
    FPS = 60
    clock = pygame.time.Clock()
    
    frameCount = 0
    loopCount = 0
    startButton = Button((255, 0, 0), 100, 100, 200, 200, 'Start')
    while True:
        frame = cat.get_image(frameCount, 25, 25, 2, (0,0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # screen.blit(Background.sprite, Background.rect)
        #draw button in the middle of the screen

        startButton.draw(screen, (0,0,0))

        

        
        
       
        pygame.display.flip()




main()