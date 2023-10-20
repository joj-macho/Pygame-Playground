import pygame
from pygame.locals import *
import sys

# Constants
# BLACK = (0, 0, 0)  
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Blank Window')  # Set the window title

    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():  # Check for events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)  # Clear the window with a dark-grey background

        # Draw all window elements

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()