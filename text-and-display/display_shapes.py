import pygame
from pygame.locals import *
import sys

# Colors
DARK_GRAY = (75, 75, 75)  # Dark-grey color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)

# Screen Dimensions
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window

# Game Settings
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to draw and display colored shapes on the screen.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Colored Shapes Display')
    clock = pygame.time.Clock()  # Clock object to control frame rate

    # Initialize variables
    font = pygame.font.Font(None, 28)  # Font for text

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements

        # Draw a line
        pygame.draw.line(window, WHITE, (50, 50), (150, 50), 3)
        text = font.render('Line', True, WHITE)
        window.blit(text, (50, 10))

        # Draw a filled and an empty rectangle
        pygame.draw.rect(window, RED, (250, 50, 100, 50), 0)  # Filled
        pygame.draw.rect(window, CYAN, (250, 200, 100, 50), 1)  # Empty 
        text = font.render('Rectangle', True, WHITE)
        window.blit(text, (250, 10))

        # Draw a filled and an empty circle
        pygame.draw.circle(window, GREEN, (450, 75), 25, 0)  # Filled
        pygame.draw.circle(window, MAGENTA, (450, 225), 25, 3)  # Empty
        text = font.render('Circle', True, WHITE)
        window.blit(text, (425, 10))
        
        # Draw a filled and an empty ellipse
        pygame.draw.ellipse(window, BLUE, (600, 50, 100, 50), 0)  # Filled
        pygame.draw.ellipse(window, ORANGE, (600, 200, 100, 50), 1)  # Empty
        text = font.render('Ellipse', True, WHITE)
        window.blit(text, (600, 10))

        # Draw a polygon
        pygame.draw.polygon(window, YELLOW, [(50, 250), (50, 220), (150, 220)])
        text = font.render('Polygon', True, WHITE)
        window.blit(text, (50, 150))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)  # Cap the frame rate to maintain a consistent speed


if __name__ == '__main__':
    main()
