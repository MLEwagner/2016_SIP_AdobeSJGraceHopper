import pygame
import random

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 108,112)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
 
LEFT = 1  
running = True 
screen = pygame.display.set_mode((700, 500)) 
pygame.display.set_caption('End-xiety')

screen.fill(BLACK)
pygame.display.flip()

font1 = pygame.font.SysFont("monospace",100)
font3 = pygame.font.SysFont("monospace",30)
font2 = pygame.font.SysFont("monospace",20)
myfont=pygame.font.SysFont("monospace",17)

def drawrect(x,y):

    pygame.draw.rect(screen, WHITE, (x, y, 170 ,45), 1)
    pygame.display.update()



while running:
    print("HI Again")
    part = 1
    while part == 1: 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0 # I also added this, it will break the main "running" while loop along with the one it's currently in (each "part") 
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: # i deleted the requirements that mouse position be greater than...
            # ...a certain x and y position, so you can click anywhere on the screen to continue. This applies to parts 1-3.
            print("You pressed the left mouse button at") # this line and the one below it are just feedback in the shell so we know it works.
            print(event.pos)
            part = 2

        # The fonts on lines 22-24 were originally here. 
        label = font1.render("End-xiety",True, WHITE)
        label2 = font3.render("Helping people understand anxiety", True, WHITE)
        label3 = font2.render("Click to continue", True, WHITE)

        screen.fill(BLACK)
        screen.blit(label, (70, 40))
        screen.blit(label2, (50, 150))
        screen.blit(label3, (240, 400))
        pygame.display.flip()


    while part == 2:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print("You pressed the leFt mouse button at")
            print(event.pos)
            part = 3 # note to me, changed this from 1 to 3 to add more parts.

        # Editing without being able to check in Pygame if this works begins here and goes down to the end
        # (except the last two lines), for the most part.
        # Text location on page definitely needs to be fixed. 
        text1 = font2.render("You are Riley, a teen who has anxiety.", True, WHITE)
        text2 = font2.render("You will catch glimpses of what a day for someone", True, WHITE)
        text4 = font2.render("who has anxiety might be like.", True, WHITE)
        text3 = font2.render("Click to continue", True, WHITE)

        screen.fill(BLACK)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 70))
        screen.blit(text4, (25, 95))
        screen.blit(text3, (240, 400))
        pygame.display.flip()
        

    while part == 3:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print("You pressed the left mouse button at")
            print(event.pos)
            print("SUCCESSSS")
            part = 4

        text1 = font2.render("Your goal is to beat the game.", True, WHITE)
        text2 = font2.render("You will have one chance to try each time it appears", True, WHITE)
        text5 = font2.render("as you progress through the story.", True, WHITE)
        text3 = font2.render("It will get easier as you go through the day", True, WHITE)
        text6 = font2.render("and learn and understand more.", True, WHITE)
        text4 = font2.render("Click to begin", True, WHITE)

        screen.fill(BLACK)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 70))
        screen.blit(text5, (25, 95))
        screen.blit(text3, (25, 135))
        screen.blit(text6, (25, 160))

        screen.blit(text4, (220, 400))
        pygame.display.flip()

    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    # Probably define the function at the top and then call it down here. 
    
    while part == 4: 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 125 and event.pos[0] < 275 and event.pos[1] > 292 and event.pos[1] < 316:
            # so now, for part 4, I made it so you have to click in a given area in the x- and y-coordinate boundaries.
            # it assumes buttons are 100 x 50 starting at (25, 300). This is probably inaccurate.
            
            print("You pressed the leFt mouse button at")
            print(event.pos)
            part = 1
            
        drawrect(45,280)
        drawrect(45,350)
        drawrect(45,420)
        
        label=myfont.render("Yo!",False,WHITE)
        screen.blit(label, (50, 292))
        label=myfont.render("Yo!",False,WHITE)
        screen.blit(label, (50, 362))
        label=myfont.render("Yo!",False,WHITE)
        screen.blit(label, (50, 432))



        # Text from section 1 of the file "Content" should be added in here and blit-ed.
        # So should the drawn rectangle to be the button. 
        # And text on top of it. 


    

        
        
    screen.fill(BLACK)
    pygame.display.flip()
    



pygame.quit()

