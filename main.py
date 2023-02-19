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

def main():
    FPS = 60
    clock = pygame.time.Clock()
    currentTime = time.time()
    firstPlay = True
    hasStarted = False
    startButton = Button.Button((96, 87, 95), 350, 250, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Start')
    pets = []
    pet = None
    while True:


        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # screen.blit(Background.sprite, Background.rect)
        #draw button in the middle of the screen
        screen.fill((157, 141, 128))
        if not hasStarted and startButton != None:
            startButton.draw(screen)

            #check if the mouse is clicked
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if startButton.getMouseClick(pos):
                    print("Clicked")
                    hasStarted = True
                    #destroy button
                    startButton = None
                    continue




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
                selected = False
                while not(selected):

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                    if pygame.mouse.get_pressed()[0]:
                        pos = pygame.mouse.get_pos()
                        for i in range(len(pets)):
                            if pos[0] > i*32 and pos[0] < i*32 + 32:
                                print("pet selected")
                                print(i)

                                #set pet
                                pet = pets[i]
                                selected = True
                                break
                    pygame.display.flip()





                # main game
                screen.fill((157, 141, 128))
                while pet.getHealth().getAmount() > 0:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()

                    healthBar = StatusBar.StatusBar(position = (20,480), text="Health", width=200)
                    fitnessBar = StatusBar.StatusBar(position = (20,520), text = "Fitness")
                    energyBar = StatusBar.StatusBar(position = (20,560), text = "Energy")
                    pet.draw(screen, 0, 25, 25, (0,0), scale=20)
                    healthBar.draw(screen)
                    fitnessBar.draw(screen)
                    energyBar.draw(screen)
                    feedButton = Button.Button((0, 255, 0), 500, 200, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Feed')
                    exerciseButton = Button.Button((0, 255, 0), 500, 400, 100, 50, "assets/fonts/Mynerve-Regular.ttf",'Exercise')
                    feedButton.draw(screen)
                    exerciseButton.draw(screen)
                    pygame.display.flip()
                ## name pet












        pygame.display.flip()




main()
