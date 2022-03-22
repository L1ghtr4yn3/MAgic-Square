import pygame
pygame.init

screenWidth = 800
screenHeight = 800
Cyan = (0, 200, 200)
xpos = 200
ypos = 400
hieght = 300
width = 300
thickness = 10

#creates game screen and caption
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("simple base code")
#game variables
doExit = False #variable to quit out of game loop

#BEGIN GAME LOOP######################################################
while not doExit:
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
    pygame.draw.rect(screen, (Cyan), (xpos, ypos, width, hieght), thickness)


    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
