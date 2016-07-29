import pygame
import random





    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)
PURPLE= (208,32,144)
GRAY = (139,137,137)

class Block(pygame.sprite.Sprite):

    def __init__(self,file_name):
        super().__init__()

        self.image = pygame.image.load(file_name)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        
    
    def update(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])


#initializing the list containing black blocks
cloud_sprite_list = pygame.sprite.Group()

#initializing the list containing green blocks
smiley_sprite_list = pygame.sprite.Group()

#initializing the list containing ALL the blocks
all_sprites_list = pygame.sprite.Group()



#initialize the player block here!
player = Block("anxiety3.png")


def make_sprites(level):

    #add the player to the list it should be in
    all_sprites_list.add(player)

    #make 50 black blocks and 50 green blocks
    for i in range(10):
        #initialize a black block
        #initalize a green block
        smiley_sprite= Block("smiley3.png")
        
        smiley_sprite.rect.x = random.randrange(screen_width, screen_width * 2)
        smiley_sprite.rect.y = random.randrange(screen_height)

        
        smiley_sprite_list.add(smiley_sprite)
        all_sprites_list.add(smiley_sprite)

    for i in range(10 * level):
        cloud_sprite= Block("clouds3.png")

        #initialize the x and y for the black block
        cloud_sprite.rect.x = random.randint(screen_width,screen_width * 2)
        cloud_sprite.rect.y = random.randint(1,500)

        #initialize the x and y for the green block


        #add the blocks to ALL the lists they should be in
        cloud_sprite_list.add(cloud_sprite)
        all_sprites_list.add(cloud_sprite)

def empty():
    all_sprites_list.empty()
    cloud_sprite_list.empty()
    smiley_sprite_list.empty()

done = False

clock = pygame.time.Clock()

#initialize the value of score
score = 0

#initialize the number of lives
lives = 3





## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)


#Call the function here that will create the blocks you want
level=1
make_sprites(level)




# Variable to check if pressing r will restart game
can_restart = False

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and can_restart:
                score = 0
                lives = 5
                level=1
                make_sprites(level)
                can_restart = False
                


 
 
    # Clear the screen
    background = pygame.image.load("anxiety.jpg")
    background= pygame.transform.scale(background,(700,500))
    rect = background.get_rect()
    screen.blit(background,(0,0))
    
    
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # Write the code to see if the player block has collided with anything
    # Check if it collides with black blocks
    # Check if it collided with green blocks
    # pygame.sprite.spritecollide might be VERY helpful. look at the example
    cloud_sprite_hit_list=pygame.sprite.spritecollide(player,cloud_sprite_list,True)
    for block in cloud_sprite_hit_list:
        lives-=1
       
    smiley_sprite_hit_list=pygame.sprite.spritecollide(player,smiley_sprite_list,True)
    for block in smiley_sprite_hit_list:
        score+=1
    
        
    
    


    # Write the code to move the blocks.
    cloud_sprite_list.update()
    smiley_sprite_list.update() 

    
 
    # Update score here
    # Collision with a certain sprite means the score should go up
    "CODE"
    

    #Update lives here
    #Collision with a certain sprite means the lives should go down
    "CODE"
    

    score_text = font.render("Score: " +str(score), True, BLACK)

    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    screen.blit(score_text, [500, 50])

    screen.blit(lives_text, [50, 50])

    ## Some logic to allow the game to be restarted
    if  len(smiley_sprite_list) == 0 and lives>=1:
        empty()
        congrats_speech=font.render("Congragulations you moved past this game!",True,BLACK)
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(congrats_speech,[150,250])
        can_restart = True
    
    if lives < 1:
        empty()
        game_over = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(game_over, [250, 250])
        can_restart = True
    

    
    # Draw all the sprites  
    all_sprites_list.draw(screen)




   
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

