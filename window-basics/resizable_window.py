import pygame
from pygame.locals import *
import sys

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to set a dynamically resizable window .'''
    # Initialize Pygame
    pygame.init()

    # Create a resizable window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption('Resizable Window')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets

    # Intitalize variables

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
