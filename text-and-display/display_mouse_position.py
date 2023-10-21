import pygame
from pygame.locals import *
import sys

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WHITE = (255, 255, 255) # Color constant for white
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to Track and display mouse position on screen'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mouse Position Tracker')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets

    # Intitalize variables

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Display mouse position
        font = pygame.font.Font(None, 48)
        text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, WHITE)
        window.blit(text, (20, 20))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
