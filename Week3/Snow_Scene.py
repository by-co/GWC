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

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Snow")


# Your SnowFlake class

class SnowFlake():
    def __init__(self, x_location, y_speed, size):
        self.x_location = x_location
        self.y_location = 0
        self.y_speed = y_speed
        self.size = size
        self.color = WHITE
    def snowFall(self, screen):
    
        if self.y_location <= 500:
            self.y_location += self.y_speed
            
        pygame.draw.circle(screen, self.color, [self.x_location, self.y_location], self.size)
      
      
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed
speed = 3

# Snow List
snow_list = []
q = 0

# for i in range(0, random.randint(25,100)):
    # snow_list.append(SnowFlake(random.randint(0, SCREEN_WIDTH), random.randint(3, 10), random.randint(1, 5)))
    
# s = SnowFlake(random.randint(10, SCREEN_WIDTH), speed, 10)   

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    # Begin Snow
    snow_list.append(SnowFlake(random.randint(0, SCREEN_WIDTH), random.randint(3, 5), random.randint(1, 5)))
    for s in snow_list:
        s.snowFall(screen)
    # s.snowFall(screen)

    # End Snow
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
