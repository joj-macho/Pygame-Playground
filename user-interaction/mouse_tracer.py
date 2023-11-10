import pygame
from pygame.locals import *
import sys

# Colors
DARK_GRAY = (75, 75, 75)
WHITE = (255, 255, 255)
CYAN = (0, 255, 255)

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game
MAX_POINTS = 42  # Maximum number of points to trace


def main():
    '''Main function to track and display mouse tracing on the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create the game window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Mouse Tracer')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Intitalize variables
    font = pygame.font.Font(None, 48)  # Font for text
    points = []  # Store points to trace
    line_width = 2  # Default line width

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()
           
            if event.type == MOUSEMOTION:
                # Append mouse position to points list and maintain a maximum number of points
                points.append(event.pos)
                if len(points) > MAX_POINTS:
                    del points[0]

            if event.type == KEYDOWN:
                # Adjust line width with the up and down arrow keys
                if event.key == K_UP:
                    line_width += 1
                elif event.key == K_DOWN:
                    line_width = max(1, line_width - 1)

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        if len(points) > 1:
            # Draw lines to trace the mouse movement
            pygame.draw.lines(window, CYAN, False, points, line_width)

        # Draw the line width on the screen
        line_width_text = font.render(f'Line Width: {line_width}', True, WHITE)
        window.blit(line_width_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
