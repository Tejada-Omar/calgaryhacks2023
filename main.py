import sys, pygame
from Pet import Pet
pygame.init()

size = width, height = 320, 240

screen = pygame.display.set_mode(size)

cat = pygame.image.load("assets/pets/placeholder.png")


def main():
    FPS = 60
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0, 0, 0))
       #screen.blit(cat, (0, 0))
        pygame.display.flip()
        



main()