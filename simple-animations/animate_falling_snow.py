import pygame
from pygame.locals import *
import sys
import random

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)  # White color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
SNOWFLAKE_SIZE = 3  # Width and height of the object
NUM_SNOWFLAKES = 100  # Number of snowflakes


def main():
    '''Main function to animate falling snow on the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Falling Snow Animation')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize snowflakes
    snowflakes = []
        
    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Generate and update snowflakes
        if len(snowflakes) < NUM_SNOWFLAKES:
            snowflakes.append({
                'x': random.randint(0, WINDOW_WIDTH),
                'y': 0,
                'speed': random.randint(1, 5)
            })

        # Iterate through the list of snowflakes to update their positions.
        for snowflake in snowflakes:
            snowflake['y'] += snowflake['speed']
            # Increment the 'y' coordinate of the snowflake, making it fall downward.
            if snowflake['y'] > WINDOW_HEIGHT:
                # Remove snowflakes after reaching screen bottom
                snowflakes.remove(snowflake)

        # Clear the window
        window.fill(DARK_GRAY)
            
        # Draw all snowflakes
        for snowflake in snowflakes:
            pygame.draw.circle(window, WHITE, (snowflake['x'], snowflake['y']), SNOWFLAKE_SIZE)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
