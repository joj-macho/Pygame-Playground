import pygame
from pygame.locals import *
import sys
from pathlib import Path


# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
IMAGE_SPEED = 5  # Number of pixels to move the image in each frame
IMG_WIDTH_HEIGHT = 100  # Width and height of the image
MAX_WIDTH = WINDOW_WIDTH - IMG_WIDTH_HEIGHT  # Maximum x-coordinate to keep image within the window
MAX_HEIGHT = WINDOW_HEIGHT - IMG_WIDTH_HEIGHT  # Maximum y-coordinate to keep image within the window

# Image paths
BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading
IMAGE_PATH = str(BASE_PATH) + '/images'
BALL_IMAGE_PATH = f'{IMAGE_PATH}/dragonball.png'
BACKGROUND_IMAGE_PATH = f'{IMAGE_PATH}/dragon_background.jpg'


def main():
    '''Main function to animate a moving image within the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing Ball Animation')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Load image assets
    image = pygame.image.load(BALL_IMAGE_PATH)
    background = pygame.image.load(BACKGROUND_IMAGE_PATH)
    
    # Initialize variables
    image_x = 100  # Initial x-coordinate of the image
    image_y = 100  # Initial y-coordinate of the image

    speed_x = IMAGE_SPEED  # Horizontal speed of the image
    speed_y = IMAGE_SPEED  # Vertical speed of the image

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Check if the image is out of the window boundaries and reverse its direction
        if (image_x < 0) or (image_x >= MAX_WIDTH):
            speed_x = -speed_x  # reverse x direction

        if (image_y < 0) or (image_y >= MAX_HEIGHT):
            speed_y = -speed_y  # reverse y direction

        # Update the image's location, adding the speed in both x and y directions
        image_x += speed_x
        image_y += speed_y

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        window.blit(background, (0, 0))  # Draw the background image
        window.blit(image, (image_x, image_y))  # Draw the image at the updated position
        
        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
