import pygame
from pygame.locals import *
import sys
import random
from snake import SnakeSegment
from food import Food

# Colors
DARK_GRAY = (75, 75, 75)

# Screen Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Game Settings
FRAMES_PER_SECOND = 30
BLOCK_SIZE = 10

def main():
    '''Main function to run the Snake Game.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Simple Snake Game')
    clock = pygame.time.Clock()

    # Initialize variables
    snake_segments = [SnakeSegment(window, 400, 300, BLOCK_SIZE)]  # Create a snake segment
    food = Food(window, WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # Handle key events for controlling the snake's direction
            if event.type == KEYDOWN:
                if event.key == K_UP and snake_segments[0].direction != 'DOWN':
                    snake_segments[0].direction = 'UP'
                elif event.key == K_DOWN and snake_segments[0].direction != 'UP':
                    snake_segments[0].direction = 'DOWN'
                elif event.key == K_LEFT and snake_segments[0].direction != 'RIGHT':
                    snake_segments[0].direction = 'LEFT'
                elif event.key == K_RIGHT and snake_segments[0].direction != 'LEFT':
                    snake_segments[0].direction = 'RIGHT'

        # Move the snake
        snake_segments[0].move()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all window elements
        food.draw()
        # Check for collisions with food
        if snake_segments[0].rect.colliderect(food.rect):
            food.spawn_food()

        for segment in snake_segments:
            segment.draw()

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()