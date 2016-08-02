import random
import pygame
import webbrowser

pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 108, 112)
GREEN = (0, 255, 0)
BLUE = (170, 208, 255)
 
LEFT = 1  
running = True 
screen = pygame.display.set_mode((700, 500)) 
pygame.display.set_caption('End-xiety')

screen.fill(BLACK)
pygame.display.flip()

font1 = pygame.font.SysFont("monospace",100)
font3 = pygame.font.SysFont("monospace",30)
font2 = pygame.font.SysFont("monospace",20)
font4 = pygame.font.SysFont("monospace",19)
myfont=pygame.font.SysFont("monospace",17)

def drawrect(x,y):
    pygame.draw.rect(screen, WHITE, (25, y, x ,45), 1)
    pygame.display.update()

############ BEGIN RUNNER GAME CLASS #############################
class Block(pygame.sprite.Sprite):

    def __init__(self,file_name):
        super().__init__()

        self.image= pygame.image.load(file_name)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def update_bad(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            '''a = random.randrange(70, 235)
            b = random.randrange(265, 500)'''
            #self.rect.y = random.choice([a, b])
            self.rect.y = random.randrange(50, 470)
            self.rect.x = screen_width + 10

    def update_good(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.y = random.randrange(60, 460)
            self.rect.x = screen_width + 10


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

#initializing the list containing BAD sprites
cloud_sprite_list = pygame.sprite.Group()

#initializing the list containing GOOD SPRITES
smiley_sprite_list = pygame.sprite.Group()

#initializing the list containing ALL SPRITES
all_sprites_list = pygame.sprite.Group()

#initialize the player block here!
player = Block("anxiety3.png")

game = True
won = False

def make_sprites(smiley_level, cloud_level):
    
    #add the player("anxiety3.png" to the list it should be in
    all_sprites_list.add(player)

    # for loop for GOOD SPRITES
    for i in range(smiley_level*10): 
        smiley_sprite = Block("smiley3.png")
        #initialize the x and y for the GOOD SPRITE
        smiley_sprite.rect.x = random.randrange(screen_width, screen_width*2)
        smiley_sprite.rect.y = random.randrange(60, screen_height-40)
        
        #add the blocks to ALL the lists they should be in
        smiley_sprite_list.add(smiley_sprite)
        all_sprites_list.add(smiley_sprite)

    #======= IF STATEMENT  =======
    if game == True:
        for i in range(cloud_level*10):
            cloud_sprite = Block("cloud3.png")
            cloud_sprite.rect.x = random.randrange(screen_width, screen_width*2)
            cloud_sprite.rect.y = random.randrange(50, 470)
            cloud_sprite_list.add(cloud_sprite)
            all_sprites_list.add(cloud_sprite)

def empty():
    all_sprites_list.empty()
    cloud_sprite_list.empty()
    smiley_sprite_list.empty()
    
def runner_game(score_num, smile_num, cloud_num):
    empty()
    runner_game_over = 2
    done = True
    won = False
    clock = pygame.time.Clock()
    #initialize the value of score
    score_num = score_num
    score = score_num #CHANGED IT TO DIVIDE BY TWO 
    # Font to allow for 
    font = pygame.font.SysFont("Gill Sans", 30, True, False)

    #Call the function here that will create the SPRITES you want
    level_c = cloud_num
    level_s = smile_num
    make_sprites(level_s, level_c)

    # Variable to check if pressing r will start game
    can_restart = False
    start = True
    number = 0 

    while done:
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    score = score_num
                    level_c = cloud_num
                    level_s = smile_num
                    make_sprites(level_s, level_c)
                    empty()
                    make_blocks()
                    can_restart = False

        
        if can_restart == False:
            # Clear the screen
            background = pygame.image.load("anxiety.jpg")
            background= pygame.transform.scale(background,(700,500))
            rect = background.get_rect()
            screen.blit(background,(0,0))
        
            # Get the current mouse position. This returns the position
            # as a list of two numbers.
            pos = pygame.mouse.get_pos()
       
            # Fetch the x and y out of the list, just like we'd fetch letters out of a string.
            # Set the player object to the mouse location
            player.rect.x = pos[0]
            player.rect.y = pos[1]
     
            # Write the code to see if the player block has collided with anything
            # pygame.sprite.spritecollide might be VERY helpful. look at the example
            cloud_sprite_hit_list = pygame.sprite.spritecollide(player, cloud_sprite_list, True)
            smiley_sprite_hit_list = pygame.sprite.spritecollide(player, smiley_sprite_list, True)

            # Write the code to move the blocks.
            for block in cloud_sprite_list:
                block.update_bad()
                if can_restart==True:
                    break 
                    
            for block in smiley_sprite_list:
                block.update_good()
                if can_restart==True:
                    break
            
            # Update score here
            # Collision with a certain sprite means the score should go up     
            for block in smiley_sprite_hit_list:
                score += 1
                number = number + 1
                if number == (smile_num*10):
                    won = True
                    break

            score_text = font.render("Life: " +str(score), True, GREEN)
            screen.blit(score_text, [300, 30])
                
            if won == True:
                screen.fill(WHITE)
                all_sprites_list.empty()
                win = font.render("YOU  WIN!!", True, BLUE)
                screen.blit(win, [300, 225])
                score_text = font.render("Life: " +str(score), True, WHITE)
                screen.blit(score_text, [300, 30])
                can_restart = True
                runner_game_over = 1
                done = False

            for block in cloud_sprite_hit_list:
                score -= 1
                if number == (smile_num*10):
                    break

    #=========== How the game ends =============
            if score < 1:
               score = 0
               score_text = font.render("Score: " +str(score), True, BLACK)
               screen.blit(score_text, [300, 30])
               screen.fill(BLACK)
               all_sprites_list.empty()
               game_over = font.render("YOU FAILED.", True, RED)
               screen.blit(game_over, [275, 225])
               runner_game_over = 0
               can_restart = True 
               done = False
    #===========================================

            # Draw all the sprites
            all_sprites_list.draw(screen)
     
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
     
            # Limit to 60 frames per second
            clock.tick(30) #35

    return runner_game_over

################ END RUNNER GAME CLASS ##################################

while running:
    print("HI Again, original code")
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
        text7 = font4.render("Use your mouse to collect all ten happy thoughts and avoid", True, BLUE)
        text8 = font4.render("gloomy ones. This game will appear randomly throughout", True, BLUE)
        text9 = font4.render("the story, and you'll get one chance to beat it each time.", True, BLUE)
        text4 = font2.render("Click to begin game", True, WHITE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 70))
        screen.blit(text5, (25, 95))
        screen.blit(text3, (25, 135))
        screen.blit(text6, (25, 160))
        screen.blit(text7, (25, 200))
        screen.blit(text8, (25, 225))
        screen.blit(text9, (25, 250))
        screen.blit(text4, (220, 400))
        pygame.display.flip()

    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    game1 = runner_game(3, 1, 13)
    screen.fill(BLACK)
    '''
    if game1 == 0:
        print("Game failed, returned back to main code")
        screen.fill(BLACK)
        print("Next part: 4")'''
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
        # drawrect(170,420) (third rect position)
        label=myfont.render("Next",False,WHITE)
        screen.blit(label, (30, 292))
        # screen.blit(label, (30, 432)) (position label for third rect)
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
        text5 = font4.render("Do they think I'm weird for being alone?", True, RED) #SIZE?
        text6 = font4.render("They don't really want to be my friend.", True, RED)
        text7 = font4.render("Maybe they're mad at me.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 100))
        screen.blit(text4, (25, 125))
        screen.blit(text5, (190, 210))
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
        text1 = font2.render("Eventually, it's break. You finally see your friends.", True, WHITE)
        text2 = font2.render("You consider asking them about this morning, but you", True, WHITE)
        text3 = font2.render("don't want to seem clingy. Your quiz is next period,", True, WHITE)
        text6 = font2.render("and you're starting to freak out. Do you...", True, WHITE)
        text4 = font4.render("If I tell them they'll be annoyed.", True, RED)
        text5 = font4.render("I am so unprepared.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text6, (25, 105))
        screen.blit(text4, (250, 260)) #REPOSITION
        screen.blit(text5, (380, 390)) #REPOSITION
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
        text2 = font4.render("Is it that obvious?", True, RED)
        text3 = font4.render("I can't lie to her and say it's nothing.", True, RED)
        #text4 = font4.render("Then she'll be really offended.", True, RED)  #DELETE
        #text5 = font4.render("She'll be annoyed by my complaints.", True, RED) #DELETE
        text4 = font4.render("I don't want her to think I'm stupid.", True, RED)
        text6 = font4.render("People with anxiety tend to worry about small concerns and", True, BLUE)
        text7 = font4.render("amplify the impact of them in their mind. Try to understand", True, BLUE)
        text8 = font4.render("where they are coming from without being belittling them.", True, BLUE)
        #text9 = font4.render("towards them.", True, BLUE) #DELETE
        screen.blit(text1, (25, 30))
        screen.blit(text10,(25, 55))
        screen.blit(text6, (25, 100))
        screen.blit(text7, (25, 125))
        screen.blit(text8, (25, 150))
        #screen.blit(text9, (25, 175))
        screen.blit(text2, (100, 224))
        screen.blit(text3, (235, 344))    
        screen.blit(text4, (270, 380))
        #screen.blit(text5, (70, 410))
        pygame.display.flip()
        
    screen.fill(BLACK)

    while part == 8: #jordan is a butt 
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
        text1 = font2.render('''"I'm going to fail my calculus quiz next period,"''', True, WHITE)
        text2 = font2.render("you mumble. You dig through your backpack for your", True, WHITE)
        text3 = font2.render("notes to do some last-minute review.", True, WHITE)
        text4 = font2.render('Jordan rolls his eyes. "Not this again."', True, WHITE)
        text5 = font4.render("I knew they wouldn't want to hear.", True, RED)
        text6 = font4.render("I shouldn't have said anything.", True, RED)
        text7 = font4.render("He doesn't like being around me.", True, RED)
        text8 = font4.render("He's only pretending to be my friend.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        screen.blit(text5, (150, 200))
        screen.blit(text6, (260, 280))
        screen.blit(text7, (40, 350))
        screen.blit(text8, (250, 430))
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
        label=myfont.render("Next (game)", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render('''"He's just upset you're doing better than him in math,"''', True, WHITE)
        text2 = font2.render('''Rory murmured, glaring at Jordan. "You'll do great, I''', True, WHITE)
        text3 = font2.render('''believe in you." You relax slightly but still don't''', True, WHITE)
        text4 = font2.render("fully believe her.", True, WHITE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        pygame.display.flip()

    #================ INSERT GAME???? ====================
    game2 = runner_game(3, 1, 10)
    screen.fill(BLACK)

    '''if game2 == (0 or 1):    
        print("Game failed, returned back to main code")
        screen.fill(BLACK)
        print("Next part: 10")'''
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
        text1 = font2.render("You walk into the classroom. The quiz is on your desk.", True, WHITE)
        text2 = font2.render("Your mind goes blank as you read the sheet. You feel", True, WHITE)
        text3 = font2.render("extremely nervous, second-guessing yourself and", True, WHITE)
        text9 = font2.render("changing answers", True, WHITE)
        text4 = font4.render("What will my parents think?", True, RED)
        text5 = font4.render("I should have studied more, I'm going to fail.", True, RED)
        text10 = font4.render("I'm going to end up homeless on the street.", True, RED) 
        text6 = font4.render("People with generalized anxiety tend to be perfectionists", True, BLUE)
        text7 = font4.render("and spend excessive time studying. However, it can cause", True, BLUE)
        text11 = font4.render("stress, leading to procrastination and lack of", True, BLUE)
        text12 = font4.render("motivation. It's important to provide reassurance about", True, BLUE)
        text8 = font4.render("their performance.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text9, (25, 105)) #IS THE SPACING FOR THIS AND THE NEXT FIVE OKAY? 
        screen.blit(text6, (25, 145))
        screen.blit(text7, (25, 170))
        screen.blit(text11, (25, 195))
        screen.blit(text12, (25, 220))
        screen.blit(text8, (25, 245))
        screen.blit(text4, (270, 330))
        screen.blit(text10, (100, 400))
        pygame.display.flip()


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
        label=myfont.render("Next (game)", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("You and Jordan meet at Rory's house before the party.", True, WHITE)
        text2 = font2.render("You look at your friends' clothes and feel overdressed.", True, WHITE)
        text3 = font4.render("Everyone will think I have no fashion sense.", True, RED)
        text4 = font4.render("I'm going to stand out in a bad way..", True, RED)
        text5 = font4.render("Individuals with social anxiety fear being in situations", True, BLUE)
        text6 = font4.render("where they may be judged. To help them, try to soothe them", True, BLUE)
        text7 = font4.render("and their worries. Don't try to change who they are.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text5, (25, 100))
        screen.blit(text6, (25, 125))
        screen.blit(text7, (25, 150))
        screen.blit(text3, (50, 400))
        screen.blit(text4, (250, 300))
        pygame.display.flip()

    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    game3 = runner_game(3, 1, 8)
    screen.fill(BLACK)

    while part == 12: #Jordan leaves them. AT PARTY NOW
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 13
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("Jordan disappears into the crowd as soon as you all", True, WHITE)
        text3 = font2.render("arrive at the party.", True, WHITE)
        text2 = font4.render("I knew he didn't want to be around me...", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text3, (25, 55))
        screen.blit(text2, (140, 200))
        pygame.display.flip()

    screen.fill(BLACK)

    while part == 13: #Riley leaves u alone
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 14
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))                  
        text1 = font2.render("You've just been with Rory so far, but now she's", True, WHITE)
        text2 = font2.render("going to the bathroom, leaving you by yourself.", True, WHITE)
        text5 = font2.render("You move to an isolated part of the room as", True, WHITE)
        text6 = font2.render("you wait for Rory.", True, WHITE)
        text7 = font4.render("Some people deal with the fear of embarrassing themselves", True, BLUE)
        text8 = font4.render("by avoiding social situations, but others might be really", True, BLUE)
        text9 = font4.render("outgoing in these situations to hide any imperfections.", True, BLUE)
        text3 = font4.render("I don't want to stand out.", True, RED)
        text4 = font4.render("They'll think I'm a loser.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text5, (25, 80))
        screen.blit(text6, (25, 105))
        screen.blit(text7, (25, 150))
        screen.blit(text8, (25, 175))
        screen.blit(text9, (25, 200))
        screen.blit(text3, (350, 270)) #######
        screen.blit(text4, (150, 400)) #######
        pygame.display.flip()

    screen.fill(BLACK)

    while part == 14: #someone says hi
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 15
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 215 and event.pos[1] > 350 and event.pos[1] < 395:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 16
        drawrect(190, 280)
        drawrect(170, 350)
        label = myfont.render('Say "Hello" back', False, WHITE)
        screen.blit(label, (30, 292))
        label = myfont.render("Walk away", False, WHITE)
        screen.blit(label, (30, 362))
        text1 = font2.render("Someone walks up to you and greets you. She seems", True, WHITE)
        text2 = font2.render("friendly. You start to feel flustered, worried that", True, WHITE)
        text3 = font2.render("you might offend them. Do you...", True, WHITE)
        text4 = font4.render("She's just talking to me because she pities me.", True, RED)
        text5 = font4.render("What if I accidentally offend her?", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (90, 190)) #####
        screen.blit(text5, (260, 330)) #####
        pygame.display.update()

    screen.fill(BLACK)
    
    #15=8a, 16=8b, 17=8c, 18=8d, 19=9
    #15->19;  16->17/18;  17->18;  18->19;
    while part == 15: #you talk to that someone
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 19
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("Even though you're nervous about talking to the", True, WHITE)
        text2 = font2.render("stranger, the two of you talk, and even find some", True, WHITE)
        text3 = font2.render("common interests.", True, WHITE)
        text4 = font4.render("People with social anxiety are unreasonably or", True, BLUE)
        text5 = font4.render("excessively afraid of being judged or criticized.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 115))
        screen.blit(text5, (25, 140))
        pygame.display.update()

    screen.fill(BLACK)

    while part == 16: #you walk away from nice person
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 17 #MAKE sure it matches buttons
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 215 and event.pos[1] > 350 and event.pos[1] < 395:
            print("You pressed the left mouse button at") 
            print(event.pos)
            part = 18
        #FIX BUTTON PARAMETERS FOR SIZE AND CLICK AND CHECK PART 14 FOR THIS TOO  
        drawrect(190, 280)
        drawrect(190, 350)
        label = myfont.render('Go look for Rory', False, WHITE)
        screen.blit(label, (30, 292))
        label = myfont.render("Stay where you are", False, WHITE)
        screen.blit(label, (30, 362))
        text1 = font2.render("You excuse yourself to the bathroom and walk away.", True, WHITE)
        text2 = font2.render("You find a quiet spot to sit and wait for Rory.", True, WHITE)
        text3 = font4.render("I hope no one notices me.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (280, 200)) #####
        pygame.display.update()

    screen.fill(BLACK)

    while part == 17: #you look for rory but go back 
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 18
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("You leave your spot to walk around the main room,", True, WHITE)
        text2 = font2.render("looking to see if Rory was out, but you can't find her.", True, WHITE)
        text3 = font2.render("You give up and return to your hidden spot.", True, WHITE)
        text4 = font4.render("That was so awkward", True, RED)
        text5 = font4.render("I hope no one saw.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (160, 195)) 
        screen.blit(text5, (346, 295))
        pygame.display.update()

    screen.fill(BLACK)

    while part == 18: #a nice person talks to you and u can't get away
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 19
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("A girl from your English class approaches you. You", True, WHITE)
        text2 = font2.render("don't know her well or feel comfortable with her, but", True, WHITE)
        text3 = font2.render("she starts talking to you about the class, and you can't", True, WHITE)
        text4 = font2.render("get away. you discover she's really nice after talking", True, WHITE)
        text5 = font2.render("to her for a few minutes.", True, WHITE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        screen.blit(text5, (25, 130))
        pygame.display.update()
    
    screen.fill(BLACK)

    while part == 19: #truth or dare
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 20
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("Rory finally returns, saying she ran into a friend", True, WHITE)
        text2 = font2.render("of hers who invited her to play Truth or Dare. She", True, WHITE)
        text3 = font2.render("asks you if you want to join. You start to shake when", True, WHITE)
        text4 = font2.render("you realize you're the center of attention.", True, WHITE)
        text5 = font4.render("Even though a lot of social anxiety is emotional, there", True, BLUE)
        text6 = font4.render("are also physical aspects, such as a faster heartbeat or", True, BLUE)
        text7 = font4.render("dizziness. The best thing you can do for someone with", True, BLUE)
        text8 = font4.render("physical symptoms is try to help them breathe and calm down.", True, BLUE)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        screen.blit(text5, (25, 150))
        screen.blit(text6, (25, 175))
        screen.blit(text7, (25, 200))
        screen.blit(text8, (25, 225))
        pygame.display.update()

    screen.fill(BLACK)

    while part == 20: #agree to play truth/dare
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 21
        drawrect(170,280)
        label = myfont.render("Next", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("You hear yourself agree--you don't want to seem", True, WHITE)
        text2 = font2.render("nervous and join under pressure--but you regret your", True, WHITE)
        text3 = font2.render("decision instantly.", True, WHITE)
        text4 = font4.render("I can't believe I said yes.", True, RED)
        text5 = font4.render("I never should have done this.", True, RED)
        text6 = font4.render("Everyone will think I'm a freak.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (290, 310))
        screen.blit(text5, (180, 210))
        screen.blit(text6, (120, 390))
        pygame.display.update()

    screen.fill(BLACK)

    while part == 21:#end party
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 22
        drawrect(170,280)
        label = myfont.render("End (game)", False, WHITE)
        screen.blit(label, (30, 292))
        text1 = font2.render("The game of truth or dare has ended. Rory says to", True, WHITE)
        text2 = font2.render('''you, "I know this wasn't easy for you, but thank you"''', True, WHITE)
        text3 = font2.render('''for going out of your comfort zone. It means a lot to''', True, WHITE)
        text4 = font2.render('''me that you could come. Everyone thought you were fun''', True, WHITE)
        text5 = font2.render('''to talk to, and they felt comfortable with you."''', True, WHITE)
        text6 = font2.render("I guess tonight could have been worse.", True, RED)
        screen.blit(text1, (25, 30))
        screen.blit(text2, (25, 55))
        screen.blit(text3, (25, 80))
        screen.blit(text4, (25, 105))
        screen.blit(text5, (25, 130))
        screen.blit(text6, (190, 190))
        pygame.display.update()

    screen.fill(BLACK) 

    tip_count = random.randint(0, 2)
    #MAKE A WHILE LOOP HERE: Put runner game in it, if they don't win, stay in
    #the while loop. If they do, then they exit the while loop. After the game
    #(if they lose) then it should be a screen that displays a tip until they
    #click a button.

    #games = runner_game(5, 1, 6)
    #the commented out block of text below would be put into the while loop
    #mentioned above for tips.

    evil_block = 7
        
    while part == 22:
        final_game = True
        evil_block -= 1
        games = runner_game(5, 1, evil_block)
        screen.fill(BLACK)
        if games == 0: #if fail game called above
            tip_count += 1
            if tip_count > 3:
                tip_count = 1
            while final_game: #screen for tip
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    running = False
                    part1 = 0
                    final_game = False
                    games == 2
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: # and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
                    print("You pressed the left mouse button at FAILED")
                    print(event.pos)
                    final_game = False #break this while loop
                    games == 2
                drawrect(170,280)
                label = myfont.render("Retry",False,WHITE)
                screen.blit(label, (30, 292))
                if tip_count == 1: 
                    text1 = font4.render("Tip: If you're willing, let the person with anxiety know", True, BLUE)
                    text2 = font4.render("you're available for them to talk, but don't force them to.", True, BLUE)
                    text3 = font4.render("", True, BLUE)
                if tip_count == 2: 
                    text1 = font4.render("Tip: Don't bring up anxiety often, you may trigger it.", True, BLUE)
                    text2 = font4.render("Instead, let them bring it up to you.", True, BLUE)
                    text3 = font4.render("", True, BLUE)
                if tip_count == 3: 
                    text1 = font4.render("Tip: Try not to get frustrated with someone who has", True, BLUE)
                    text2 = font4.render("anxiety. It can be difficult to control the disorder,", True, BLUE)
                    text3 = font4.render("and it makes it hard to think logically.", True, BLUE)
                screen.blit(text1, (25, 30))
                screen.blit(text2, (25, 55))
                screen.blit(text3, (25, 80))
            #break
        elif games == 1:
            while final_game: 
                event = pygame.event.poll()
                if event.type == pygame.QUIT:
                    running = False
                    part = 0
                    final_game = False
                    games == 2
                    print("GAME IS ALMOST OVER")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
                    print("You pressed the left mouse button at")
                    print(event.pos)
                    part = 23
                    final_game = False
                    games == 2
                drawrect(170,280)
                label = myfont.render("More information", False, WHITE)
                screen.blit(label, (30, 292))

                text1 = font4.render("Riley eventually accepts her anxiety and reaches out for", True, WHITE) #include link to a tinyurl with list of links so people can check it out?
                text2 = font4.render("help. She learns to manage it and gets better with the", True, WHITE)
                text3 = font4.render("support of friends and family. She learns to voice her", True, WHITE)
                text4 = font4.render("discomfort more often and not let people like Jordan make", True, WHITE)
                text5 = font4.render("her feel like anxiety isn't a real problem. She is facing", True, WHITE)
                text6 = font4.render("her challenges and fighting to conquer them.", True, WHITE)
                screen.blit(text1, (25, 30))
                screen.blit(text2, (25, 55))
                screen.blit(text3, (25, 80))
                screen.blit(text4, (25, 105))
                screen.blit(text5, (25, 130))
                screen.blit(text6, (25, 155))
                pygame.display.update()

    screen.fill(BLACK)

    if part > 0:
        webbrowser.open("endxiety.github.io")
    
    while part == 23:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
            part = 0
            '''
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: # and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
            print("You pressed the left mouse button at")
            print(event.pos)
            part = 23
            final_game = False
            games == 2
            '''
            text1 = font2.render("More links and information: endxiety.github.io", True, WHITE)
            screen.blit(text1, (25, 30))
            pygame.display.update()


    print("END")
    
    pygame.display.flip()

    running = False
    
pygame.display.update()
pygame.quit()

