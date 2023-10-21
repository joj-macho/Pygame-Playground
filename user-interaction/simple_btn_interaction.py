import pygame
from pygame.locals import *
import sys

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
RED = (255, 0, 0)
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game
BUTTON_WIDTH = 200  # Button width
BUTTON_HEIGHT = 100  # Button height

def main():
    '''Main function to handle simple button interaction.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simple Button Interaction')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets

    # Initialize variables
    button_rect = pygame.Rect((WINDOW_WIDTH - BUTTON_WIDTH) // 2, (WINDOW_HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Initialize clicks counter
    click_count = 0   

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            # Detect and Handle button clicks
            if event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    click_count += 1 

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        pygame.draw.rect(window, RED, button_rect)  # Draw the button

        # Render the text
        font = pygame.font.Font(None, 36)
        text = font.render(f'{click_count} Button Clicks', True, (255, 255, 255))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
