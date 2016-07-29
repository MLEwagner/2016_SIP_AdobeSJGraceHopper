import pygame
import random

    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 108, 112)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

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

def make_sprites(level):

    #add the player("anxiety3.png" to the list it should be in
    all_sprites_list.add(player)

    # for loop for GOOD SPRITES
    for i in range(10): 
        smiley_sprite = Block("smiley3.png")
        #initialize the x and y for the GOOD SPRITE
        smiley_sprite.rect.x = random.randrange(screen_width, screen_width*2)
        smiley_sprite.rect.y = random.randrange(50, screen_height)
        
        #add the blocks to ALL the lists they should be in
        smiley_sprite_list.add(smiley_sprite)
        all_sprites_list.add(smiley_sprite)

    #=========== IF STATEMENT  =======================
    if game == True:
        for i in range(level*10):
            cloud_sprite = Block("cloud3.png")
            cloud_sprite.rect.x = random.randrange(screen_width, screen_width*2)
            cloud_sprite.rect.y = random.randrange(50, 500)
            cloud_sprite_list.add(cloud_sprite)
            all_sprites_list.add(cloud_sprite)


def empty():
    all_sprites_list.empty()
    cloud_sprite_list.empty()
    smiley_sprite_list.empty()
    

done = True

clock = pygame.time.Clock()

#initialize the value of score
score = 4

# Font to allow for 
font = pygame.font.SysFont("Gill Sans", 30, True, False)

#Call the function here that will create the SPRITES you want
level = 7
make_sprites(level)

# Variable to check if pressing r will start game
can_restart = False
start = True
number = 0 

while done:
    for event in pygame.event.get():    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                score = 4
                level = 7
                make_sprites(level)
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
            if number == 10:                
                won = True
                break

        score_text = font.render("Score: " +str(score), True, GREEN)
        screen.blit(score_text, [300, 30])
            
        if won == True:
            screen.fill(WHITE)
            all_sprites_list.empty()
            win = font.render("YOU  WIN!!", True, BLUE)
            screen.blit(win, [300, 225])
            score_text = font.render("Score: " +str(score), True, WHITE)
            screen.blit(score_text, [300, 30])
            can_restart = True

        for block in cloud_sprite_hit_list:
            score -= 2
            if number == 10:
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
           can_restart = True 
          # done = False
#===========================================

     
        # Draw all the sprites
        all_sprites_list.draw(screen)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(60)

pygame.quit()
exit()
