import pygame
from pygame.locals import *
import sys
from snow import Snowflake

# Constants
BLACK = (0, 0, 0)  # Black color constant
WHITE = (255, 255, 255)  # White color constant
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game
NUM_SNOWFLAKES = 100  # Number of snows to generate

def main():
    '''Main function to run the snow animation.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Falling Snow Animation')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Create a Snowflake object
    snowflakes = [Snowflake(window, WINDOW_WIDTH, WINDOW_HEIGHT) for _ in range(NUM_SNOWFLAKES)]

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Clear the window
        window.fill(BLACK)

        # Update and draw snowflakes
        for snowflake in snowflakes:
            snowflake.update(WINDOW_HEIGHT)
            snowflake.draw(window)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
