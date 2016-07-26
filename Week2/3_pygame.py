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

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
CIRCLE_X = int(SCREEN_WIDTH/2)
CIRCLE_Y = int(SCREEN_HEIGHT/2)

# ** STEP 2 **
# SIZE = 30
COLOR = BLUE

# ** STEP 3 **
# CHANGE_X = 10
# CHANGE_Y = 10

# ** STEP 5 **
CHANGE_X = random.randint(-10, 10)
CHANGE_Y = random.randint(-10, 10)

# ** STEP 6 **
SIZE = random.randint(20, 80)

# ** STEP 7 **
MAGENTA = (255, 51, 153)
ORANGE = (255, 153, 51)
YELLOW = (255, 255, 153)
MINT = (153, 255, 204)
FOREST = (0, 102, 0)
TIFFANY_BLUE = (129, 216, 208)
SKY_BLUE = (102, 153, 255)

COLOR_LIST = [BLACK, WHITE, GREEN, GREY,
YELLOW, RED, BLUE, MAGENTA, ORANGE,
MINT, FOREST, TIFFANY_BLUE, SKY_BLUE]

i = 0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    # --- Screen-clearing code goes here
    # ** STEP 1 ** 
    screen.fill(GREEN)

    # --- Drawing code should go here

    # ** STEP 2 **
    pygame.draw.circle(screen, COLOR, (CIRCLE_X, CIRCLE_Y), SIZE, 0)

    # ** STEP 3 **
    # (CIRCLE_X, CIRCLE_Y) = pygame.mouse.get_pos()

    # ** STEP 4 **
    if CIRCLE_X < 0 or CIRCLE_X > SCREEN_WIDTH:
        CHANGE_X = -CHANGE_X
    if CIRCLE_Y < 0 or CIRCLE_Y > SCREEN_HEIGHT:
        CHANGE_Y = -CHANGE_Y
    CIRCLE_X += CHANGE_X
    CIRCLE_Y += CHANGE_Y

    # ** STEP 7 **
    COLOR = COLOR_LIST[random.randint(0,len(COLOR_LIST)-1)]

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
