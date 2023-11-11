import pygame
from pygame.locals import *
import sys


# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
RED = (255, 0, 0)  # Red color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
OBJECT_SPEED = 8  # Number of pixels to move the object
OBJECT_SIZE = 25  # Width and height of the object
MAX_WIDTH = WINDOW_WIDTH - OBJECT_SIZE  # Maximum x-coordinate to keep object within the window
MAX_HEIGHT = WINDOW_HEIGHT - OBJECT_SIZE  # Maximum y-coordinate to keep object within the window


def main():
    '''Main function to animate a moving object within the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing Circle Animation')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize object position and speed
    object_x, object_y = 50, 50
    object_speed_x, object_speed_y = OBJECT_SPEED, OBJECT_SPEED

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()     

        # Bounce the object when it reaches screen borders
        if object_x < OBJECT_SIZE or object_x >= MAX_WIDTH:
            object_speed_x = -object_speed_x
        if object_y < OBJECT_SIZE or object_y >= MAX_HEIGHT:
            object_speed_y = -object_speed_y

        # Update object position
        object_x += object_speed_x
        object_y += object_speed_y

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the circle object
        pygame.draw.circle(window, RED, (object_x, object_y), OBJECT_SIZE)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
