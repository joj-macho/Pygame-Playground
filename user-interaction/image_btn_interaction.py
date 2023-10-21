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
    '''Main function to handle button interaction.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Image Button Interaction')

    # Create a clock object to control frame rate
    clock = pygame.time.Clock()

    # Load assets
    path_to_on_btn = str(BASE_PATH) + '/images/toggle-on.png'
    button_up_image = pygame.image.load(path_to_on_btn)

    path_to_off_btn = str(BASE_PATH) + '/images/toggle-off.png'
    button_down_image = pygame.image.load(path_to_off_btn)

    # Initialize variables
    button_rect = button_up_image.get_rect()
    button_rect.topleft = ((WINDOW_WIDTH - button_rect.width) // 2, (WINDOW_HEIGHT - button_rect.height) // 2)

    # Initialize clicks counter
    click_count = 0   

    button_pressed = False

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
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

        # Handle game logic

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        # Draw the button
        if button_pressed:
            window.blit(button_down_image, button_rect.topleft)
        else:
            window.blit(button_up_image, button_rect.topleft)

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
