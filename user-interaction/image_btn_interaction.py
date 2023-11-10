import pygame
from pygame.locals import *
import sys
from pathlib import Path

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)  # White color

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
IMAGE_SPEED = 5  # Number of pixels to move the image in each frame

# Image paths
BASE_PATH = Path(__file__).resolve().parent  # Base path for asset loading
IMAGE_PATH = str(BASE_PATH) + '/images'
BTN_UP_IMAGE_PATH = f'{IMAGE_PATH}/toggle-on.png'
BTN_DOWN_IMAGE_PATH = f'{IMAGE_PATH}/toggle-off.png'


def main():
    '''Main function to handle button interaction.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Image Button Interaction')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Load image assets
    button_up_image = pygame.image.load(BTN_UP_IMAGE_PATH)
    button_down_image = pygame.image.load(BTN_DOWN_IMAGE_PATH)

    # Initialize variables
    font = pygame.font.Font(None, 36)  # Font for text
    button_rect = button_up_image.get_rect()  # Button rectangle
    button_rect.topleft = ((WINDOW_WIDTH - button_rect.width) // 2, (WINDOW_HEIGHT - button_rect.height) // 2)

    # Initialize button state
    button_pressed = False

    # Initialize clicks counter
    click_count = 0   

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            # Detect and handle button clicks
            if event.type == MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    click_count += 1
                    button_pressed = True
            elif event.type == MOUSEBUTTONUP:
                button_pressed = False

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the button state
        if button_pressed:
            window.blit(button_down_image, button_rect.topleft)
        else:
            window.blit(button_up_image, button_rect.topleft)

        # Draw the text
        text = font.render(f'{click_count} Button Clicks', True, WHITE)
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, 50))
        window.blit(text, text_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
