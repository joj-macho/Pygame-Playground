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
    '''Main function to animate a moving image on the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Animate Moving Image')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load image assets
    path_to_image = str(BASE_PATH) + '/images/dragonball.png'
    image = pygame.image.load(path_to_image)

    path_to_background = str(BASE_PATH) + '/images/dragon_background.jpg'
    background = pygame.image.load(path_to_background)
    
    # Initialize variables
    IMG_WIDTH_HEIGHT = 100  # Width and height of the image
    MAX_WIDTH = WINDOW_WIDTH - IMG_WIDTH_HEIGHT  # Maximum X-coordinate to keep image within the window
    MAX_HEIGHT = WINDOW_HEIGHT - IMG_WIDTH_HEIGHT  # Maximum Y-coordinate to keep image within the window

    image_x = 100  # Initial X-coordinate of the image
    image_y = 100  # Initial Y-coordinate of the image

    speed_x = IMAGE_SPEED  # Horizontal speed of the image
    speed_y = IMAGE_SPEED  # Vertical speed of the image

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic
        # Check if the image is out of the window boundaries and reverse its direction
        if (image_x < 0) or (image_x >= MAX_WIDTH):
            speed_x = -speed_x  # reverse X direction

        if (image_y < 0) or (image_y >= MAX_HEIGHT):
            speed_y = -speed_y  # reverse Y direction

        # Update the image's location, adding the speed in both X and Y directions
        image_x += speed_x
        image_y += speed_y

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        window.blit(background, (0, 0))  # Draw the background image
        window.blit(image, (image_x, image_y))  # Blit the image at the updated position
        
        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
