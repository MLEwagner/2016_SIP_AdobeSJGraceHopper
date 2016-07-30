import random
import pygame

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 108,112)
GREEN = (0, 255, 0)
BLUE = (170, 208, 255)
 
LEFT = 1  
running = True 
screen = pygame.display.set_mode((700, 500)) 
pygame.display.set_caption('End-xiety')

screen.fill(BLACK)
pygame.display.flip()
'''
font1 = pygame.font.SysFont("comicsansms",100)
font3 = pygame.font.SysFont("comicsansms",30)
font2 = pygame.font.SysFont("comicsansms",20)
font4 = pygame.font.SysFont("comicsansms",19)
myfont=pygame.font.SysFont("comicsansms",17)
'''
font1 = pygame.font.SysFont("monospace",100)
font3 = pygame.font.SysFont("monospace",30)
font2 = pygame.font.SysFont("monospace",20)
font4 = pygame.font.SysFont("monospace",19)
myfont=pygame.font.SysFont("monospace",17)


def drawrect(x,y):

    pygame.draw.rect(screen, WHITE, (25, y, x ,45), 1)
    pygame.display.update()



while running:
    print("HI Again")
    part = 1
    screen.fill(BLACK)
    
    while part == 1: #home screen
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
        screen.blit(label, (70, 40))
        screen.blit(label2, (50, 150))
        screen.blit(label3, (240, 400))
        pygame.display.flip()

    screen.fill(BLACK)
    
    while part == 2: #overview
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 3 # note to me, changed this from 1 to 3 to add more parts.
        text1 = font2.render("You are Riley, a teen who has anxiety.", True, WHITE)
        text2 = font2.render("You will catch glimpses of what a day for someone", True, WHITE)
        text4 = font2.render("who has anxiety might be like.", True, WHITE)
        text3 = font2.render("Click to continue", True, WHITE)
        text5 = font2.render("Everyone worries sometimes, but anxiety is a disorder", True, BLUE)
        text6 = font2.render("that causes exccessive worrying.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 70))
        screen.blit(text4, (25, 95))
        screen.blit(text5, (25, 170))
        screen.blit(text6, (25, 195))
        screen.blit(text3, (240, 400))
        pygame.display.flip()
        
    screen.fill(BLACK)
    
    while part == 3: #game intro
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 4
        text1 = font2.render("Your goal is to beat the game.", True, WHITE)
        text2 = font2.render("You will have one chance to try each time it appears", True, WHITE)
        text5 = font2.render("as you progress through the story.", True, WHITE)
        text3 = font2.render("It will get easier as you go through the day", True, WHITE)
        text6 = font2.render("and learn and understand more.", True, WHITE)
        text4 = font2.render("Click to begin", True, WHITE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 70))
        screen.blit(text5, (25, 95))
        screen.blit(text3, (25, 135))
        screen.blit(text6, (25, 160))
        screen.blit(text4, (220, 400))
        pygame.display.flip()

    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    # Probably define the function at the top and then call it down here. 

    screen.fill(BLACK)
    
    while part == 4: #wake up
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            # so now, for part 4, I made it so you have to click in a given area in the x- and y-coordinate boundaries.
            # it assumes buttons are 100 x 50 starting at (25, 300). This is probably inaccurate.
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 5
        drawrect(170,280)
        # drawrect(25,350)
        # drawrect(25,420)
        label=myfont.render("Next",False,WHITE)
        screen.blit(label, (30, 292))
        # label=myfont.render("Yo!",False,WHITE)
        # screen.blit(label, (30, 362))
        # label=myfont.render("Yo!",False,WHITE)
        # screen.blit(label, (30, 432)                                          #
        text1 = font2.render("You wake up to the sound of your alarm. The first", True, WHITE)
        text2 = font2.render("thing that comes to your mind is your quiz later", True, WHITE)
        text3 = font2.render("in the day. And then a party at night you have to", True, WHITE)
        text4 = font2.render("attend.", True, WHITE)
        text5 = font2.render("I'm going to fail.", True, RED)
        text6 = font4.render("None of my studying will pay off.", True, RED)
        text8 = font4.render("Four hours of studying wasn't enough", True, RED)
        text9 = font4.render("The quiz'll hurt my grade a lot.", True, RED)
        text7 = font4.render("The party's going to be awkward.", True, RED)        
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        screen.blit(text9, (290, 230))
        screen.blit(text5, (350, 280))
        screen.blit(text6, (160, 360))
        screen.blit(text8, (120, 390))
        screen.blit(text7, (310, 460))
        pygame.display.flip()
        
    screen.fill(BLACK)
    
    while part == 5: #get to school
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 6
        drawrect(170,280)
        label=myfont.render("Next",False,WHITE)
        screen.blit(label, (30, 292))                                          #
        text1 = font2.render("You arrive to school. You don't see either of your", True, WHITE)
        text2 = font2.render("friends.", True, WHITE)
        text3 = font4.render("It's normal for people with generalized anxiety to worry", True, BLUE)
        text4 = font4.render("about things that seem mundane.", True, BLUE)
        text5 = font4.render("Are they avoiding me?", True, RED)
        text6 = font4.render("They don't really want to be my friend.", True, RED)
        text7 = font4.render("Everyone's judging me now.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 100))
        screen.blit(text4, (25, 125))
        screen.blit(text5, (380, 240))
        screen.blit(text6, (220, 310))
        screen.blit(text7, (100, 400))
        pygame.display.flip() 

    screen.fill(BLACK)
    
    while part == 6: #start of brunch
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 7
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 335 and event.pos[1] > 350 and event.pos[1] < 395:
            # PART 7B, ADJUST RANGE FOR MOUSECLICK HERE AND ABOVE
            part = 8
        drawrect(170,280)
        drawrect(310,350) #FIRST PARAMETER WAS 170
        label=myfont.render("Say nothing",False,WHITE)
        screen.blit(label, (30, 292))     
        label=myfont.render("Tell them how worried you are",False,WHITE)
        screen.blit(label, (30, 362))
        text1 = font2.render("Eventually, it's brunch. You finally see your friends.", True, WHITE)
        text2 = font2.render("Your quiz is next period, and you're starting to", True, WHITE)
        text3 = font2.render("freak out. Do you...", True, WHITE)
        text4 = font4.render("If I tell them they'll be annoyed.", True, RED)
        text5 = font4.render("I am so unprepared.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (250, 270)) #REPOSITION
        screen.blit(text5, (380, 420)) #REPOSITION
        pygame.display.flip()

    screen.fill(BLACK)

    while part == 7: #rory's like whats up 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 8
        drawrect(170,280)
        label=myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render('''Rory looks at you funny. "What's wrong? Why are you''', True, WHITE)
        text10 = font2.render('''so jittery?''', True, WHITE)
        text2 = font4.render("Is it that obvious?", True, WHITE)
        text3 = font4.render("I can't lie to her and say it's nothing.", True, RED)
        text4 = font4.render("Then she'll be really offended.", True, RED)
        text5 = font4.render("She'll be annoyed by my complaints.", True, RED)
        text6 = font4.render("People with anxiety tend to worry about small concerns and", True, BLUE)
        text7 = font4.render("amplify the impact of them in their mind. Try to understand", True, BLUE)
        text8 = font4.render("where they are coming from without being disparaging", True, BLUE)
        text9 = font4.render("towards them.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text10,(25, 55))
        screen.blit(text6, (25, 145))
        screen.blit(text7, (25, 170))
        screen.blit(text8, (25, 195))
        screen.blit(text9, (25, 220))
        #screen.blit(text2, (
        #screen.blit(text3, (    
        #screen.blit(text4, (
        #screen.blit(text5, (
        pygame.display.flip()
        
    screen.fill(BLACK)

    while part == 8: #jordan is a dick pt 1 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 9
        drawrect(170,280)
        label=myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render('''I'm going to fail my calculus quiz next period."''', True, WHITE)
        text2 = font2.render("You mumble. You dig through your backpack for your", True, WHITE)
        text3 = font2.render("notes to do somelast-minute review.", True, WHITE)
        text4 = font2.render('Jordan rolls his eyes. "Not this again."', True, WHITE)
        text5 = font4.render("I knew they wouldn't want to hear.", True, RED)
        text6 = font4.render("I shouldn't have said anything.", True, RED)
        text7 = font4.render("He doesn't like being around me.", True, RED)
        text8 = font4.render("He's only pretending to be my friend.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        #screen.blit(text5, (
        #screen.blit(text6, (
        #screen.blit(text7, (
        #screen.blit(text8, (
        pygame.display.flip()

    screen.fill(BLACK)

    while part == 9: #rory is encouraging 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 10
        drawrect(170,280)
        label=myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        #text1 = font2.render("ENCOURAGEMENT FROM RORY", True, WHITE)
        #text2 = font4.render("TIPS", True, WHITE)
        #screen.blit(text1, (25, 30))
        #screen.blit(text2, (25,
        pygame.display.flip()

    screen.fill(BLACK)

    while part == 10: #test happens
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 11
        drawrect(170,280)
        label=myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("You walk into the classroom. The quiz is on your desk.Your", True, WHITE)
        text2 = font2.render("mind goes blank as you read the sheet. You feel extremely", True, WHITE)
        text3 = font2.render("nervous.", True, WHITE)
        text4 = font4.render("I know all this but still can't do it.", True, RED)
        text5 = font4.render("I didn't study enough,", True, RED)
        text6 = font4.render("Students with generalized anxiety tend to be perfectionists", True, BLUE)
        text7 = font4.render("and spend excessive time studying. It's important to provide", True, BLUE)
        text8 = font4.render("comfort and reassurance about their performance.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text6, (25, 195))
        screen.blit(text7, (25, 220))
        screen.blit(text8, (25, 245))
        #screen.blit(text3, (
        #screen.blit(text4, (
        pygame.display.flip()


    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    

    screen.fill(BLACK)
    
    while part == 11: #test happens
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 12
        drawrect(170,280)
        label=myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("You and Jordan meet at Rory's house before the party. You", True, WHITE)
        text2 = font2.render("look at your friends' clothes and feel overdressed.", True, WHITE)
        text3 = font4.render("Everyone will think I have no fashion sense.", True, RED)
        text4 = font4.render("I'm going to stand out in a bad way..", True, RED)
        text5 = font4.render("Individuals with social anxiety fear being in situations", True, BLUE)
        text6 = font4.render("where they may be judged. To help them, try to soothe them", True, BLUE)
        text7 = font4.render("and their worries. Don't try to change who they are.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text5, (25, 170))
        screen.blit(text6, (25, 195))
        screen.blit(text7, (25, 220))
        #screen.blit(text3, (
        #screen.blit(text4, (
        pygame.display.flip()
        

    screen.fill(BLACK)
    pygame.display.flip()
    

pygame.quit()

