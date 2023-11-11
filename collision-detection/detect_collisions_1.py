import pygame
from pygame.locals import *
import sys

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)  # Dark-grey color
RED = (255, 0, 0)  # Red color
GREEN = (0, 255, 0)  # Green color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
PLAYER_SPEED = 5  # Number of pixels to move the player circle
PLAYER_RADIUS = 20  # Radius of the player circle
TARGET_RADIUS = 15  # Radius of the target circle


def main():
    '''Main function for simple collision detection.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Collision Detection')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize variables
    player_x, player_y = 100, 100
    target_x, target_y = 400, 300
    collision_count = 0  # Initialize collision counter
    font = pygame.font.Font(None, 36)  # Text for font

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()    

        # Handle continuous key presses events
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys_pressed[K_RIGHT]:
            player_x += PLAYER_SPEED
        if keys_pressed[K_UP]:
            player_y -= PLAYER_SPEED
        if keys_pressed[K_DOWN]:
            player_y += PLAYER_SPEED

        # Check for collision
        distance = ((player_x - target_x) ** 2 + (player_y - target_y) ** 2) ** 0.5
        if distance < (PLAYER_RADIUS + TARGET_RADIUS):
            collision_count += 1

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        pygame.draw.circle(window, RED, (player_x, player_y), PLAYER_RADIUS)  # Draw a red circle representing the player
        pygame.draw.circle(window, GREEN, (target_x, target_y), TARGET_RADIUS)  # Draw a green circle representing the target

        # Display Collision text
        text = font.render(f'Collision Detected ({collision_count} collisions)', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
