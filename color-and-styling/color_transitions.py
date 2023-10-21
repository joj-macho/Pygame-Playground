import pygame
from pygame.locals import *
import sys
import math

# Constants
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game

def main():
    '''Main function to demonstrate color transitions in Pygame.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Color Transitions')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets

    # Initialize variables
    time_passed = 0

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic
        # Calculate color based on time
        red = int((math.sin(time_passed) + 1) * 127.5)
        green = int((math.cos(time_passed) + 1) * 127.5)
        blue = int((math.sin(time_passed + math.pi) + 1) * 127.5)

        # Update time passed
        time_passed += 0.01

        # Clear the window
        # Fill the window with the calculated color
        window.fill((red, green, blue))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)

if __name__ == '__main__':
    main()
