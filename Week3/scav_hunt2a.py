"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)



pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.location = location # tuple
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, ball_color, self.location, self.ball_size)


# -------- Main Program Loop -----------
ball = BouncingBall(350, 250, 10, 10, 30)
ball2 = BouncingBall(200, 398, 5, 5, 50)
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here
    mouse_pressed = pygame.mouse.get_pressed() #booleans in a tuple (button1, button2, button3)
    mouse_position = pygame.mouse.get_pos() #tuple value
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE) 
    # --- Drawing code should go here
    
    font = pygame.font.Font(None, 80)   #create new Font object
    text = "Hello!"                     #set string 
    size = font.size(text)              #set size using Font.size method
    ren = font.render(text, 0, BLACK, WHITE)    #create new Surface to render text
    
    if mouse_pressed[0]:
        screen.blit(ren, (10, 10))  #blit text onto the screen at (10, 10)
    
    
    ball.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball2.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


