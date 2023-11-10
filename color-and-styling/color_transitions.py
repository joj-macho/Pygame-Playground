import pygame
from pygame.locals import *
import sys
import math

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to demonstrate color transitions in Pygame.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Color Transitions')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize variables
    time_passed = 0  # Init time counter

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Calculate color based on time
        red = int((math.sin(time_passed) + 1) * 127.5)
        green = int((math.cos(time_passed) + 1) * 127.5)
        blue = int((math.sin(time_passed + math.pi) + 1) * 127.5)

        # Update time passed
        time_passed += 0.01

        # Fill the window with the calculated color
        window.fill((red, green, blue))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
