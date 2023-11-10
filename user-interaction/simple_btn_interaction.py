import pygame
from pygame.locals import *
import sys

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)  # White color
RED = (255, 0, 0)  # Red color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
IMAGE_SPEED = 5  # Number of pixels to move the image in each frame

# Button Dimensions
BUTTON_WIDTH = 200  # Button width
BUTTON_HEIGHT = 100  # Button height


def main():
    '''Main function to handle simple button interaction.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simple Button Interaction')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize variables
    font = pygame.font.Font(None, 36)  # Font for text
    button_rect = pygame.Rect((WINDOW_WIDTH - BUTTON_WIDTH) // 2, (WINDOW_HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)  # Button rectangle

    # Initialize clicks counter
    click_count = 0   

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            # Detect and Handle button clicks
            if event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    click_count += 1 

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        pygame.draw.rect(window, RED, button_rect)  # Draw the button

        # Draw the text
        font = pygame.font.Font(None, 36)
        text = font.render(f'{click_count} Button Clicks', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
