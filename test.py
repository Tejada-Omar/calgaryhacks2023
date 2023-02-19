import sys, pygame
import classes.StatusBar as StatusBar

pygame.init()

size = width, height = 400, 400

screen = pygame.display.set_mode(size)

def main():
    FPS = 60
    clock = pygame.time.Clock()

    while True:     
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        healthBar = StatusBar.StatusBar(text="Health")
        healthBar.setPercent(0.9)
        healthBar.draw(screen)

        pygame.display.flip()
main()