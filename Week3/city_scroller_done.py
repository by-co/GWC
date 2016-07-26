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
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(→).
            A negative integer draws the building left to right (←).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up ↑
            A negative integer draws the building down ↓
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width   = width
        self.height  = height
        self.color   = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height])

    def move(self, speed):
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right →
            A negative integer moves the building to the left  ←
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """
        self.x_point -= speed



class Scroller(object):
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.

    Other info:
        It has an instance variable "buildings" which is a list of buildings for the scroller
    """

    def __init__(self, width, height, base, color, speed):
        self.width  = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.building_list = [] # instance variable "buildings": list of buildings for scroller object
        self.add_buildings() # populate the Scroller object with buildings each time a new instance is created

    def add_buildings(self):
        """
        Will add a randomly generated building that fits within the width and height
        of the scroller. Uses add_building method.
        """
        current_width = 0 # keep track of scroller width
        while current_width <= self.width: # stop when scroller is wide as screen
            self.add_building(current_width) # calling the add_building method; note "self"
            """
            self.building_list ------------- list of building objects
            self.building_list[-1] --------- the last item in the list (most recently created)
            self.building_list[-1].width --- the width of the last item
            """
            current_width += self.building_list[-1].width # update the scroller width

    def add_building(self, x_location):
        """
        takes in an x_location (an integer) which represents where along the x-axis to
        put a building.
        Adds a building to list of buildings.
        """
        # The building width will be a random integer between 1/20th and 1/4th of the width
        building_width = random.randint((self.width // 20), (self.width // 4))
        
        # The max height of each building is the difference btwn scroller base (floor) & height (ceiling)
        max_height = self.base - self.height 

        # The building height will be a random integer between 1/4th and the max_height
        building_height = random.randint((max_height // 4), max_height)

        # The top of the building is the difference between scroller base (floor) and building height 
        y_location = self.base - building_height

        self.building_list.append(Building(x_location, y_location, building_width, building_height, self.color))

    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        # draw every building in the scroller
        for building in self.building_list:
            building.draw()

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable.

        ** As the buildings move off the screen a new one is added. **
        """
        # move every building in the scroller
        for building in self.building_list:
            building.move(self.speed)

        # save the X-coordinate of the end of the scroller (add x_point of the LAST building and its WIDTH)
        new_building_location = self.building_list[-1].x_point + self.building_list[-1].width

        # ADD one new building to the scroller AT the end of the scroller
        self.add_building(new_building_location)

# ------- Create Scroller Instances ----------

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 400, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
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
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code should go here

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
