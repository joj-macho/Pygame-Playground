import pygame
from pygame.locals import *
import sys
from pathlib import Path
import math

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
PLAYER_SPEED = 5  # Number of pixels to move the character

# Image Paths
BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + '/images'


def main():
    '''Main function to simulate the movement of a character using various images to create realistic animation.'''

    # Initialize Pygame
    pygame.init()
    
    # Create the game window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Realistic Character Movement')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate
    
    # Load the player character's image
    player_img = pygame.image.load(f'{IMAGE_PATH}/person_down_1.png')

    # Initialize player character's position and direction
    player_rect = player_img.get_rect()

    MAX_WIDTH = WINDOW_WIDTH - player_rect.width
    MAX_HEIGHT = WINDOW_HEIGHT - player_rect.height
    player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)  # Center starting position
    direction = 'down'  # Initial direction

    player_step_count = 0  # Init step count
    moving = False  # Init starting movement
    
    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Check for direction keys pressed
        keys_pressed = pygame.key.get_pressed()
        moving_left = keys_pressed[K_LEFT]
        moving_right = keys_pressed[K_RIGHT]
        moving_up = keys_pressed[K_UP]
        moving_down = keys_pressed[K_DOWN]

        # Determine new direction based on pressed keys
        if moving_left:
            new_direction = 'left'
            moving = True
        elif moving_right:
            new_direction = 'right'
            moving = True
        elif moving_up:
            new_direction = 'up'
            moving = True
        elif moving_down:
            new_direction = 'down'
            moving = True
        else:
            new_direction = direction
            moving = False  # Set moving to False when no key is pressed
        
        # Simulate character animation based on the movement direction
        if moving:
            step_delay = 3  # Step delay to control animation speed
            player_step_count += 1  # Increment step count

            # Reset the step count when it exceeds the maximum number of steps
            if player_step_count >= 4 * step_delay:
                player_step_count = 1

            # Calculate the current animation step
            player_step_position = math.floor(player_step_count / step_delay) + 1

            # Load the character image corresponding to the new direction and step position
            player_img = pygame.image.load(f'{IMAGE_PATH}/person_{new_direction}_{player_step_position}.png')

            # Update the current direction
            direction = new_direction
        else:
            player_step_count = 0  # Reset step count when not moving

         # Move the character if the corresponding key is pressed
        if moving_left:
            player_rect.move_ip(-PLAYER_SPEED, 0)
        if moving_right:
            player_rect.move_ip(PLAYER_SPEED, 0)
        if moving_up:
            player_rect.move_ip(0, -PLAYER_SPEED)
        if moving_down:
            player_rect.move_ip(0, PLAYER_SPEED)
        
        # Keep the character within the window bounds
        player_rect.y = max(0, min(MAX_HEIGHT, player_rect.y))
        player_rect.x = max(0, min(MAX_WIDTH, player_rect.x))

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the player character
        window.blit(player_img, player_rect)

        # Update the display
        pygame.display.update()
        
        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
