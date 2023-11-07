import pygame
from pygame.locals import *
import sys
from dvd_logo import DVDLogo  # Import the DVDLogo class from dvd_logo.py

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WHITE = (255, 255, 255)  # Color constant for white
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game

def main():
    '''Main program to animate bouncing DVD logos of various colors.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing DVD Logos')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Create a list of DVDLogo objects with various colors
    colors = [
        (255, 0, 0),  # Red
        (0, 255, 0),  # Green
        (0, 0, 255),  # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (255, 165, 0)  # Orange
    ]

    dvd_logos = [DVDLogo(window, WINDOW_WIDTH, WINDOW_HEIGHT, color) for color in colors]

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update and draw all DVDLogos
        window.fill(DARK_GRAY)  # Clear the window

        for dvd_logo in dvd_logos:
            dvd_logo.update()
            dvd_logo.draw()
            font = pygame.font.Font(None, 24)
            text = font.render(f'Corner Hits: {dvd_logo.hits}', True, WHITE)
            window.blit(text, (dvd_logo.logo_x, dvd_logo.logo_y))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
