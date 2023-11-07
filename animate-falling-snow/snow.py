import pygame
import random

class Snowflake:
    '''Class to represent the snowflake in the animation.'''

    def __init__(self, window, window_width, window_height):
        '''
        Initialize a snowflake object.

        Parameters:
            window (pygame.Surface): The window to draw into.
            window_width (int): The width of the window.
            window_height (int): The height of the window.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        # Initialize x and y positions
        self.x = random.randint(0, self.window_width)
        self.y = random.randint(0, self.window_height)

        # Snow falling speed
        self.speed = random.randint(1, 5)
        # Size of the snowflake
        self.size = random.randint(2, 5)
        # White color
        self.color = (255, 255, 255)

    def update(self, window_height):
        '''Move the snowflake down and wrap it to the top if it reaches the bottom.'''
        self.y += self.speed
        if self.y > self.window_height:
            self.y = 0
            self.x = random.randint(0, self.window_width)

    def draw(self, screen):
        '''Draw the snowflake on the screen.'''
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.size)
