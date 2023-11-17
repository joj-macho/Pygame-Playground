import pygame
from pygame.locals import *

# Colors
BLACK = (0, 0, 0)  # Block color constant

class Player:
    def __init__(self, window, window_width, window_height, x, y, size):
        '''
        Initialize the Player object.

        Parameters:
            - window: Pygame window surface.
            - window_width: Width of the window.
            - window_height: Height of the window.
            - x: Initial x-coordinate of the player.
            - y: Initial y-coordinate of the player.
            - size: Size of the player's block.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.x = x
        self.y = y
        self.size = size

        # Create a rectangle representing the player's block
        self.rect = pygame.Rect(x, y, size, size)

        # Set the player's speed
        self.speed = 8

    def move(self, keys_pressed):
        '''Move the player based on the keys pressed.'''

        # Check if left arrow key or 'A' key is pressed and player is not at the left edge
        if (keys_pressed[K_LEFT] or keys_pressed[K_a]) and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)  # Move the player left

        # Check if right arrow key or 'D' key is pressed and player is not at the right edge
        if (keys_pressed[K_RIGHT] or keys_pressed[K_d]) and self.rect.right < self.window_width:
            self.rect.move_ip(self.speed, 0)  # Move the player right

        # Check if up arrow key or 'W' key is pressed and player is not at the top edge
        if (keys_pressed[K_UP] or keys_pressed[K_w]) and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)  # Move the player up

        # Check if down arrow key or 'S' key is pressed and player is not at the bottom edge
        if (keys_pressed[K_DOWN] or keys_pressed[K_s]) and self.rect.bottom < self.window_height:
            self.rect.move_ip(0, self.speed)  # Move the player down

    def draw(self):
        '''Draw the player's block on the window.'''
        pygame.draw.rect(self.window, BLACK, self.rect)
