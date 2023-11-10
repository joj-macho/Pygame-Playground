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

# Image paths
BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading
IMAGE_PATH = str(BASE_PATH) + '/images'
BALL_IMAGE_PATH = f'{IMAGE_PATH}/dragonball.png'
BACKGROUND_IMAGE_PATH = f'{IMAGE_PATH}/dragon_background.jpg'


def main():
    '''Main function to handle on-click key presses.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('On Click Key Presses')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Load image assets
    image = pygame.image.load(BALL_IMAGE_PATH)
    background = pygame.image.load(BACKGROUND_IMAGE_PATH)
    
    # Initialize variables
    image_x = 100  # Initial x-coordinate of the image
    image_y = 100  # Initial y-coordinate of the image

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            # Handle arrow key presses
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    image_x -= IMAGE_SPEED
                elif event.key == K_RIGHT:
                    image_x += IMAGE_SPEED
                elif event.key == K_UP:
                    image_y -= IMAGE_SPEED
                elif event.key == K_DOWN:
                    image_y += IMAGE_SPEED

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        window.blit(background, (0, 0))  # Draw the background image
        window.blit(image, (image_x, image_y))  # Draw the image
        
        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
