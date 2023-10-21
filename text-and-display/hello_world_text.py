import pygame
from pygame.locals import *
import sys

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WHITE = (255, 255, 255) # Color constant for white
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to display 'Hello, World!' in the middle of the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hello World Display')

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
        window.fill(DARK_GRAY)  # Clear the window with a dark-grey background

        # Draw all window elements
        # Display "Hello, World!" text
        font = pygame.font.Font(None, 48)
        text = font.render("Hello, World!", True, WHITE)
        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()