import pygame
from pygame.locals import *
import sys
from pathlib import Path


# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game
IMAGE_SPEED = 5  # Speed / Number of pixels to move the image

BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading


def main():
    '''Main function to handle on-click key presses.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('On Click Key Presses')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load image assets
    path_to_image = str(BASE_PATH) + '/images/dragonball.png'
    image = pygame.image.load(path_to_image)

    path_to_background = str(BASE_PATH) + '/images/dragon_background.jpg'
    background = pygame.image.load(path_to_background)
    
    # Initialize variables
    image_x = 100  # Initial X-coordinate of the image
    image_y = 100  # Initial Y-coordinate of the image

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            # Handle game logic
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:  # left arrow key press
                    image_x -= IMAGE_SPEED
                elif event.key == K_RIGHT:  # right arrow key press
                    image_x += IMAGE_SPEED
                elif event.key == K_UP:  # up arrow key press
                    image_y -= IMAGE_SPEED
                elif event.key == K_DOWN:  # down arrow key press
                    image_y += IMAGE_SPEED


        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        window.blit(background, (0, 0))  # Draw the background image
        window.blit(image, (image_x, image_y))  # Blit the image at init position
        
        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
