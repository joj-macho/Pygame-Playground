import pygame
from pygame.locals import *
import sys
import math
from pathlib import Path

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
PLAYER_SPEED = 5  # Number of pixels to move the character

# Sprite sheet layout
NUM_DIRECTIONS = 8  # Number of rows in the sprite sheet for different directions
NUM_FRAMES_PER_DIRECTION = 4  # Number of frames per direction

# Image Paths
BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + '/images'


def main():
    '''Main function to simulate the movement of a character using a sprite sheet to create realistic animation.'''
    
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Realistic Character Movement with Sprite Sheet')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Load image assets
    sprite_sheet = load_sprite_sheet(f'{IMAGE_PATH}/Civilian1(black)_Move.png', NUM_DIRECTIONS, NUM_FRAMES_PER_DIRECTION)

    # Set the initial character position and direction
    player_rect = sprite_sheet[0].get_rect()  # Get the rectangle for the character sprite
    player_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)  # Center starting position
    direction = 'north'  # Initial direction

    # Animation-related variables
    player_step_count = 0
    player_step_position = 0
    moving = False  # Check if the player is moving
    
    # Apply the scale factor to the character's image
    player_scale_factor = 2.5  # Adjust this factor to make the character larger
    player_rect.width *= player_scale_factor
    player_rect.height *= player_scale_factor

    MAX_WIDTH = WINDOW_WIDTH - player_rect.width
    MAX_HEIGHT = WINDOW_HEIGHT - player_rect.height
    
    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
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
            new_direction = 'west'
            moving = True
        elif moving_right:
            new_direction = 'east'
            moving = True
        elif moving_up:
            new_direction = 'north'
            moving = True
        elif moving_down:
            new_direction = 'south'
            moving = True
        else:
            new_direction = direction
            moving = False
        
        # Simulate character animation based on the movement direction
        if moving:
            step_delay = 5  # Step delay to control animation speed
            player_step_count += 1  # Increment step count

            # Reset the step count when it exceeds the maximum number of steps
            if player_step_count >= NUM_FRAMES_PER_DIRECTION * step_delay:
                player_step_count = 1
            
            # Calculate the current animation step
            player_step_position = math.floor(player_step_count / step_delay)
            # Update the current direction
            direction = new_direction
        else:
            player_step_count = 0  # Reset step count when not moving
        
        # Calculate the frame index based on the direction and animation step
        frame_index = ['south', 'southeast', 'east', 'northeast', 'north', 'northwest', 'west', 'southwest'].index(direction) * NUM_FRAMES_PER_DIRECTION + player_step_position

        player_img = sprite_sheet[frame_index]  # Get the current frame
        player_img = pygame.transform.scale(player_img, (player_rect.width, player_rect.height))  # Scale the player image
        
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
        window.blit(player_img, player_rect)  # Draw the character sprite
        
        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


def load_sprite_sheet(filename, rows, cols):
    '''Load a sprite sheet and divide it into individual frames.

    Parameters:
        filename (str): The file path to the sprite sheet image.
        rows (int): The number of rows in the sprite sheet.
        cols (int): The number of columns in the sprite sheet.

    Returns:
        List[pygame.Surface]: A list of individual frames from the sprite sheet.
    '''
    sprite_sheet = pygame.image.load(filename)
    sprite_width = sprite_sheet.get_width() // cols
    sprite_height = sprite_sheet.get_height() // rows
    sprite_list = []
    for row in range(rows):
        for col in range(cols):
            frame_rect = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
            sprite_list.append(sprite_sheet.subsurface(frame_rect))
    return sprite_list


if __name__ == '__main__':
    main()
