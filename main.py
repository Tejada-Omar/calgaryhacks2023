import sys, pygame
import Pet
import Background
pygame.init()

size = width, height = 400, 400

screen = pygame.display.set_mode(size)

cat = Pet.Pet(spriteSheet = "assets/pets/catOrange.png")
background = Background.Background("assets/background.png", (0,0))

def main():
    FPS = 60
    clock = pygame.time.Clock()
    frame_count = 0
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
        screen.fill((0, 0, 0))
        # screen.blit(Background.sprite, Background.rect)
        cat.draw(screen, frame_count, 25, 25, 2, -1)
        pygame.display.flip()




main()