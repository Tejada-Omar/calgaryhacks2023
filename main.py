import sys, pygame
import classes.Pet as Pet
import classes.Button as Button
import classes.StatusBar as StatusBar
import Background
import time
import os
pygame.init()

size = width, height = 800, 600

screen = pygame.display.set_mode(size)

background = Background.Background("assets/background.png", (0,0))

def startGame(startButton):
    if startButton != None:
        startButton.draw(screen)

        #check if the mouse is clicked
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if startButton.getMouseClick(pos):
                print("Clicked")
                #destroy button
                startButton = None
                return True

def main():
    FPS = 60
    clock = pygame.time.Clock()
    firstPlay = True
    hasStarted = False
    startButton = Button.Button((96, 87, 95), 350, 250, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Start')
    pet = None
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen.blit(Background.sprite, Background.rect)
        #draw button in the middle of the screen
        screen.fill((157, 141, 128))
        if not hasStarted and startGame(startButton):
            hasStarted = True
            continue

        # main game loop
        if hasStarted:
            if firstPlay:
                ## pick pet
                ## look through assets/pets
                folder = "assets/pets"
                pets = []
                for filename in os.listdir(folder):
                    if filename.endswith(".png"):
                        surface = pygame.image.load(os.path.join(folder, filename)).convert_alpha()
                        pets.append(Pet.Pet(surface))

                        print(filename)
                screen.fill((157, 141, 128))
                #draw pet selection screen
                for i in range(len(pets)):
                    pets[i].draw(screen, 0, 25, 25, (i*150-20, 200), 10)
                    print(i)

                #halt program until user selects pet
                selected = False
                while not(selected):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        for i in range(len(pets)):
                            if pos[0] > i*150-20 and pos[0] < i*150-20 + 150:
                                print("pet selected")
                                print(i)

                                #set pet
                                pet = pets[i]
                                selected = True
                                break
                    pygame.display.flip()

                # main game
                healthBar = StatusBar.StatusBar(position = (20,480), text="Health")
                fitnessBar = StatusBar.StatusBar(position = (20,520), text = "Fitness")
                feedButton = Button.Button((0, 255, 0), 500, 100, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Feed')
                exerciseButton = Button.Button((0, 255, 0), 500, 300, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Exercise')
                startTime = time.time()
                hunger = pygame.USEREVENT + 0
                fitness = pygame.USEREVENT + 1
                pygame.time.set_timer(hunger, 1000)
                pygame.time.set_timer(fitness, 1000)
                while fitnessBar.percent > 0 and healthBar.percent > 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == hunger:
                            healthBar.percent -= 0.01
                        if event.type == fitness:
                            fitnessBar.percent -= 0.01
                    screen.fill((157, 141, 128))
                    pet.draw(screen, 0, 25, 25, (0,0), scale=20)
                    healthBar.draw(screen)
                    fitnessBar.draw(screen)
                    feedButton.draw(screen)
                    exerciseButton.draw(screen)
                    currentTime = time.time()
                    counter = pygame.font.Font("assets/fonts/Mynerve-Regular.ttf", 32).render(f"Seconds Alive: {int((currentTime-startTime))}", 1, (0,0,0))
                    screen.blit(counter, (500, 500))
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        if feedButton.getMouseClick(pos):
                            healthBar.setPercent(1)
                        if exerciseButton.getMouseClick(pos):
                            fitnessBar.setPercent(1)
                    pygame.display.flip()

                screen.fill((157, 141, 128))
                restartButton = Button.Button((0, 0, 255), 350, 275, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Play Again?')
                restartButton.draw(screen)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        if restartButton.getMouseClick(pos):
                            break
                    pygame.display.flip()


                ## name pet

        pygame.display.flip()

main()
