import pygame
from pygame.locals import *
import sys

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to demonstrate creating a gradient background in Pygame.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Gradient Background')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Create a gradient using the window width and height
        for y in range(WINDOW_HEIGHT):
            color = (0, y // 3, y // 3)  # Adjust color based on y position
            pygame.draw.line(window, color, (0, y), (WINDOW_WIDTH, y))  # Draw gradient

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
