import pygame
import random

# Colors
GREEN = (0, 255, 0)  # Food color constant

class Food:
    def __init__(self, window, window_width, window_height, size):
        '''
        Initialize the Food object.

        Parameters:
            - window: Pygame window surface.
            - window_width: Width of the window.
            - window_height: Height of the window.
            - size: Size of the food block.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.size = size

        # Initialize the food position with random coordinates
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.spawn_food()

        # Initialize the time-to-live (TTL) for the food
        self.ttl = random.randint(7 * 30, 10 * 30)  # Random time between 7 and 10 seconds (converted to frames)

    def spawn_food(self):
        '''Spawn the food at a random position within the window boundaries.'''
        self.rect.x = random.randint(0, self.window_width - self.size)
        self.rect.y = random.randint(0, self.window_height - self.size)

    def update(self):
        '''Update the time-to-live (TTL) for the food.'''
        self.ttl -= 1

    def should_remove(self):
        '''Check if the food should be removed based on the TTL.'''
        return self.ttl <= 0

    def draw(self):
        '''Draw the food on the window'''
        pygame.draw.rect(self.window, GREEN, self.rect)

