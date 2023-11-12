import pygame
from pygame.locals import *
import sys
from dvd_logo import DVDLogo

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main program to animate bouncing DVD logos of various colors.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing DVD Logos')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate)

    # Create a list of DVDLogo objects with various colors
    colors = [RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, ORANGE]

    # Text for font
    font = pygame.font.Font(None, 24)

    dvd_logos = [DVDLogo(window, WINDOW_WIDTH, WINDOW_HEIGHT, color) for color in colors]

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Clear the window
        window.fill(DARK_GRAY)

        # Update and draw all window elements
        for dvd_logo in dvd_logos:
            dvd_logo.update()
            dvd_logo.draw()
            text = font.render(f'Corner Hits: {dvd_logo.hits}', True, WHITE)
            window.blit(text, (dvd_logo.logo_x, dvd_logo.logo_y))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
