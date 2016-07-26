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
CIRCLE_X = 350
CIRCLE_Y = 250

CHANGE_X = 10
CHANGE_Y = 10
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            CIRCLE_X = pygame.mouse.get_pos()[0]
            CIRCLE_Y = pygame.mouse.get_pos()[1]

    # --- Game logic should go here
    COLOR = GREY
    # --- Screen-clearing code goes here


    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(COLOR)

    # --- Drawing code should go here
    pygame.draw.circle(screen, WHITE, (CIRCLE_X, CIRCLE_Y), 30)
    if CIRCLE_X > SCREEN_WIDTH or CIRCLE_X < 0:
        CHANGE_X = -CHANGE_X 
    if CIRCLE_Y > SCREEN_HEIGHT or CIRCLE_Y < 0:
        CHANGE_Y = -CHANGE_Y
    CIRCLE_X += CHANGE_X
    CIRCLE_Y += CHANGE_Y


    # CIRCLE_X, CIRCLE_Y = CIRCLE_X + CHANGE, CIRCLE_Y + CHANGE
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
