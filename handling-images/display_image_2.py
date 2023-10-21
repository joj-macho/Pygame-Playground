import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game

BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading


def main():
    '''Main function to display an image and a background image on the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Display Image')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load image assets
    path_to_image = str(BASE_PATH) + '/images/dragonball.png'
    image = pygame.image.load(path_to_image)

    path_to_background = str(BASE_PATH) + '/images/dragon_background.jpg'
    background = pygame.image.load(path_to_background)

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
        window.blit(background, (0, 0))  # Draw the background image
        window.blit(image, (400, 30))  # Blit the image at position (400, 30)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
