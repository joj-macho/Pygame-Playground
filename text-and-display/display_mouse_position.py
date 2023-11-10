import pygame
from pygame.locals import *
import sys

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255) # White color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to track and display mouse position on screen'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mouse Position Tracker')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize variables
    font = pygame.font.Font(None, 48)  # Font for text

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Clear the window
        window.fill(DARK_GRAY)        

        # Draw mouse position
        text = font.render(f'Mouse Position: ({mouse_x}, {mouse_y})', True, WHITE)
        window.blit(text, (20, 20))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
