import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game

BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading

def main():
    '''Main function to play sound.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simple Sound Play')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load a sound asset
    path_to_sound = str(BASE_PATH) + '/sounds/whip-01.wav'
    sound = pygame.mixer.Sound(path_to_sound)

    # Intitalize variables

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                # Play the sound when spacebar is pressed
                sound.play()

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
