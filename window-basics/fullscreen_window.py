import pygame
from pygame.locals import *
import sys

# Colors 
DARK_GRAY = (75, 75, 75)  # Dark grey color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to set the Pygame window to fullscreen mode.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption('Fullscreen Window')  # Set the window title
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Clear the window with a dark-grey background
        window.fill(DARK_GRAY)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
