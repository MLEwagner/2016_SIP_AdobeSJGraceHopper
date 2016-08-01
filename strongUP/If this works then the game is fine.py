import random
import pygame

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

    def update(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            a = random.randrange(70, 235)
            b = random.randrange(265, 500)
            self.rect.y = random.choice([a, b])
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
        smiley_sprite.rect.y = random.randrange(50, screen_height)
        
        #add the blocks to ALL the lists they should be in
        smiley_sprite_list.add(smiley_sprite)
        all_sprites_list.add(smiley_sprite)

    #=========== IF STATEMENT  =======================
    if game == True:
        for i in range(cloud_level*10):
            cloud_sprite = Block("cloud3.png")
            cloud_sprite.rect.x = random.randrange(screen_width, screen_width*2)
            cloud_sprite.rect.y = random.randrange(50, 500)
            cloud_sprite_list.add(cloud_sprite)
            all_sprites_list.add(cloud_sprite)

def empty():
    all_sprites_list.empty()
    cloud_sprite_list.empty()
    smiley_sprite_list.empty()
    
def runner_game(score_num, smile_num, cloud_num):
    runner_game_over = False
    done = True
    won = False
    clock = pygame.time.Clock()
    #initialize the value of score
    score = score_num
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
                block.update()
                if can_restart==True:
                    break 
                    
            for block in smiley_sprite_list:
                block.update()
                if can_restart==True:
                    break
            
            # Update score here
            # Collision with a certain sprite means the score should go up     
            for block in smiley_sprite_hit_list:
                score += 2
                number = number + 1
                if number == (smile_num*10):
                    won = True
                    break

            score_text = font.render("Score: " +str(score), True, GREEN)
            screen.blit(score_text, [300, 30])
                
            if won == True:
                screen.fill(WHITE)
                all_sprites_list.empty()
                win = font.render("YOU  WIN!!", True, BLUE)
                screen.blit(win, [300, 225])
                runner_game_over = True
                score_text = font.render("Score: " +str(score), True, WHITE)
                screen.blit(score_text, [300, 30])
                can_restart = True

            for block in cloud_sprite_hit_list:
                score -= 2
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
               runner_game_over = True
               can_restart = True 
               done = False
    #===========================================

         
            # Draw all the sprites
            all_sprites_list.draw(screen)
     
            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
     
            # Limit to 60 frames per second
            clock.tick(60)

    return runner_game_over

################ END RUNNER GAME CLASS ##################################


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

    print ("out of part 4. about to create runner game")


    # === IMPORTANT ========= RUNNER GAME GOES HERE =================
    game = runner_game(4, 1, 7)

    if game == True:
        print ("game failed. returned back to main code")
        screen.fill(BLACK)
        print("Next Stage")
        while part == 4: #wake up
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                running = False
                part = 0
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT: #and event.pos[0] > 25 and event.pos[0] < 195 and event.pos[1] > 280 and event.pos[1] < 325:
                # so now, for part 4, I made it so you have to click in a given area in the x- and y-coordinate boundaries.
                # it assumes buttons are 100 x 50 starting at (25, 300). This is probably inaccurate.
                print("You pressed the left mouse button at")
                print(event.pos)
                part = 1
                drawrect(170,280)
                label=myfont.render("Next",False,WHITE)
                screen.blit(label, (30, 292))
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
    pygame.display.flip()

pygame.quit()
exit()
