import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)  # Dark-grey color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
BALL_SPEED = 5  # Number of pixels to move the image

# Image paths
BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading
IMAGE_PATH = str(BASE_PATH) + '/images'
BALL_IMAGE_PATH = f'{IMAGE_PATH}/dragonball.png'
TARGET_IMAGE_PATH = f'{IMAGE_PATH}/target-1.png'


def main():
    '''Main function for collision detection with images.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Collision Detection with Images')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Load image assets
    ball_image = pygame.image.load(BALL_IMAGE_PATH)
    target_image = pygame.image.load(TARGET_IMAGE_PATH)

    # Initialize variables
    ball_x, ball_y = 100, 100
    target_x, target_y = 400, 300

    # Create a Rect for collision detection
    ball_rect = ball_image.get_rect()
    ball_rect.topleft = (ball_x, ball_y)

    target_rect = target_image.get_rect()
    target_rect.topleft = (target_x, target_y)

    # Text for font
    font = pygame.font.Font(None, 36)  

    # Initialize collision counter
    collision_count = 0

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle continuous key presses events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            ball_x -= BALL_SPEED
        if keys_pressed[K_RIGHT]:
            ball_x += BALL_SPEED
        if keys_pressed[K_UP]:
            ball_y -= BALL_SPEED
        if keys_pressed[K_DOWN]:
            ball_y += BALL_SPEED

        # Update ball Rect position
        ball_rect.topleft = (ball_x, ball_y)

        # Check for collision
        if ball_rect.colliderect(target_rect):
            collision_count += 1

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        window.blit(ball_image, ball_rect)
        window.blit(target_image, target_rect)

        # Draw the text
        text = font.render(f'Collision Detected ({collision_count} collisions)', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
