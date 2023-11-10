import pygame
from pygame.locals import *
import sys
import random

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''
    Main function to display a continuous random pixel color pattern.
    '''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Random Pixel Colors')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Generate random pixel colors
        random_pixel_colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        window.lock()

        # Create random pixels
        for _ in range(42):
            random_pixel_position = (random.randint(0, WINDOW_WIDTH - 1), random.randint(0, WINDOW_HEIGHT - 1))
            window.set_at(random_pixel_position, random_pixel_colors)

        window.unlock()

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
