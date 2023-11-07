import pygame
from pygame.locals import *
import sys
from ball import Ball  # Import the Ball class from ball.py

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WHITE = (255, 255, 255)  # Color constant for white
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to run the ball animation.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bouncing Ball Animation')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Create a Ball object
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

    # Initialize a font for text
    font = pygame.font.Font(None, 36)

    # Instructions for the user
    instructions = [
        'Press SPACE to toggle pause and resume.',
        'Press R to restart the animation.',
        'Press Q to quit the program.',
    ]

    # Initial state
    paused = False
    toggle_text = 'PAUSED: OFF'

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Toggle pause
                    paused = not paused
                    toggle_text = 'PAUSED: ON' if paused else 'PAUSED: OFF'
                if event.key == pygame.K_r:
                    # Restart by recreating the ball
                    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # Update ball state
        if not paused:
            ball.update()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the ball
        ball.draw()

        # Display instructions
        y_offset = 10
        for text in instructions:
            text_surface = font.render(text, True, (255, 255, 255))
            window.blit(text_surface, (10, y_offset))
            y_offset += text_surface.get_height()

        # Display pause toggle
        toggle_surface = font.render(toggle_text, True, (255, 0, 0) if paused else (0, 255, 0))
        window.blit(toggle_surface, (WINDOW_WIDTH - toggle_surface.get_width() - 10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
