import pygame
import random
# importing the Scroller to use as background
from scroller import Scroller as Scroller



    
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= 3
        if self.rect.x < 0:
            self.rect.y = random.randrange(0, screen_height)
            self.rect.x = screen_width + 10


pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

black_block_list = pygame.sprite.Group()

green_block_list = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
player = Block(RED, 20, 15)

def make_blocks():

    all_sprites_list.add(player)
    
    for i in range(50):   
        black_block = Block(BLACK, 20, 15)
        green_block = Block(GREEN, 20, 15)
        
        black_block.rect.x = random.randrange(screen_width, screen_width * 2)
        black_block.rect.y = random.randrange(screen_height)

        green_block.rect.x = random.randrange(screen_width, screen_width * 2)
        green_block.rect.y = random.randrange(screen_height)

        black_block_list.add(black_block)
        green_block_list.add(green_block)
        all_sprites_list.add(black_block)
        all_sprites_list.add(green_block)






done = False

clock = pygame.time.Clock()

score = 0

lives = 5

## The scroller object is created here
any_scroller = Scroller(screen_width, 300, screen_height, (255, 100, 100), 2)

## Font to allow for 
font = pygame.font.SysFont("Gill Sans", 25, True, False)

# Blocks for first run of game
make_blocks()

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
                all_sprites_list.empty()
                make_blocks()
                can_restart = False
                


 
 
    # Clear the screen
    screen.fill(WHITE)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    pos = pygame.mouse.get_pos()
 
    # Fetch the x and y out of the list,
       # just like we'd fetch letters out of a string.
    # Set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
 
    # See if the player block has collided with anything.
    black_blocks_hit_list = pygame.sprite.spritecollide(player, black_block_list, True)
    green_blocks_hit_list = pygame.sprite.spritecollide(player, green_block_list, True)

    # Move the blocks.
    black_block_list.update()
    green_block_list.update()
 
    # Check the list of collisions.
    for block in green_blocks_hit_list:
        score += 1

    for block in black_blocks_hit_list:
        lives -= 1

    score_text = font.render("Score: " +str(score), True, BLACK)

    lives_text = font.render("Lives: "+ str(lives), True, BLUE)

    screen.blit(score_text, [500, 50])

    screen.blit(lives_text, [50, 50])

    ## Some logic to allow the game to be restarted
    if  len(green_block_list) == 0:
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(play_again, [250, 250])
        can_restart = True
    
    if lives < 1:
        play_again = font.render("Press 'r' to play again", True, BLACK)
        screen.blit(play_again, [250, 250])
        can_restart = True
    
    # Draw the scrolling background
    any_scroller.draw_buildings(screen)
    any_scroller.move_buildings()

    
    # Draw all the sprites  
    all_sprites_list.draw(screen)




   
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
exit()

