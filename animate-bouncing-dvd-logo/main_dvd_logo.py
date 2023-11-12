import pygame
from pygame.locals import *
import sys
from dvd_logo import DVDLogo

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
SILVER = (192, 192, 192)  # Silver color
WHITE = (255, 255, 255)  # White color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main program to animate a bouncing DVD logo.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing DVD Logo')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate)

    # Create a DVDLogo object
    dvd_logo = DVDLogo(window, WINDOW_WIDTH, WINDOW_HEIGHT, SILVER)

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Update the DVDLogo
        dvd_logo.update()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the DVDLogo
        dvd_logo.draw()

        # Display the corner hit count
        font = pygame.font.Font(None, 24)
        text = font.render(f'Corner Hits: {dvd_logo.hits}', True, WHITE)
        window.blit(text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
