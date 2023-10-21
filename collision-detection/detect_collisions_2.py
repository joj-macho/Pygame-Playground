import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game
BALL_SPEED = 5  # Number of pixels to move the image

BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading


def main():
    '''Main function for collision detection with images.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Collision Detection with Images')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets
    path_to_ball = str(BASE_PATH) + '/images/dragonball.png'
    ball_image = pygame.image.load(path_to_ball)

    path_to_target = str(BASE_PATH) + '/images/target-1.png'
    target_image = pygame.image.load(path_to_target)

    # Initialize variables
    ball_x, ball_y = 100, 100
    target_x, target_y = 400, 300

    # Create a Rect for collision detection
    ball_rect = ball_image.get_rect()
    ball_rect.topleft = (ball_x, ball_y)

    target_rect = target_image.get_rect()
    target_rect.topleft = (target_x, target_y)

    # Initialize collision counter
    collision_count = 0

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic

        # Handle continuous key presses events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:  # left arrow key press
            ball_x -= BALL_SPEED
        if keys_pressed[K_RIGHT]:  # right arrow key press
            ball_x += BALL_SPEED
        if keys_pressed[K_UP]:  # up arrow key press
            ball_y -= BALL_SPEED
        if keys_pressed[K_DOWN]:  # down arrow key press
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

        # Render the text
        font = pygame.font.Font(None, 36)
        text = font.render(f"Collision Detected ({collision_count} collisions)", True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)

if __name__ == '__main__':
    main()
