import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255) # White color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game

# Sound paths
BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading
SOUND_PATH = str(BASE_PATH) + '/sounds/whip-01.wav'


def main():
    '''Main function to play sound.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simple Sound Play')
    clock = pygame.time.Clock()  # Clock object to control frame rate)

    # Load a sound asset
    sound = pygame.mixer.Sound(SOUND_PATH)

    # Initialize variables
    font = pygame.font.Font(None, 48)  # Font for text

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN and event.key == K_SPACE:
                # Play the sound when spacebar is pressed
                sound.play()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw instruction text
        text = font.render('Press space-bar to play sound.', True, WHITE)
        window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
