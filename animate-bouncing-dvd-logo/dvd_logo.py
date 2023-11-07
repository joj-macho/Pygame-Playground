import pygame
from pygame.locals import *
import random

class DVDLogo:
    '''Class to represent the dvd logo in the animation.'''

    def __init__(self, window, window_width, window_height, dvd_color, logo_width=150, logo_height=60):
        '''
        Initialize the DVDLogo object.

        Parameters:
            window (pygame.Surface): The Pygame surface where the DVD logo is drawn.
            window_width (int): Width of the window.
            window_height (int): Height of the window.
            logo_width (int, optional): Width of the DVD logo. Default is 150.
            logo_height (int, optional): Height of the DVD logo. Default is 60.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.logo_width = logo_width
        self.logo_height = logo_height
        self.dvd_color = dvd_color

        # Initial position the DVD logo 
        self.max_width = self.window_width - self.logo_width
        self.max_height = self.window_height - self.logo_height
        self.logo_x = random.randrange(0, self.max_width)
        self.logo_y = random.randrange(0, self.max_height)

        # Initial speed of the DVD logo
        self.logo_speed_x = random.randint(2, 8)
        self.logo_speed_y = random.randint(2, 8)

        # Counter for corner hits
        self.hits = 0  

    def update(self):
        '''Update the position of the DVD logo based on its speed.'''
        # Update logo position
        self.logo_x += self.logo_speed_x
        self.logo_y += self.logo_speed_y

        # Check for corner hits and count them
        if (self.logo_x == 0 and self.logo_y == 0) or (self.logo_x == 0 and self.logo_y == self.max_height) \
                or (self.logo_x == self.max_width and self.logo_y == 0) \
                or (self.logo_x == self.max_width and self.logo_y == self.max_height):
            self.hits += 1
            # Bounce when a corner is hit
            self.logo_speed_x = -self.logo_speed_x
            self.logo_speed_y = -self.logo_speed_y
        else:
            # Bounce off the screen edges
            if self.logo_x <= 0 or self.logo_x >= self.max_width:
                self.logo_speed_x = -self.logo_speed_x
            if self.logo_y <= 0 or self.logo_y >= self.max_height:
                self.logo_speed_y = -self.logo_speed_y


    def draw(self):
        '''Draw the DVD logo on the window.'''
        # Draw the DVD-like logo
        pygame.draw.ellipse(self.window, self.dvd_color, (self.logo_x, self.logo_y, self.logo_width, self.logo_height))
        pygame.draw.rect(self.window, (0, 0, 0), (self.logo_x, self.logo_y, self.logo_width, self.logo_height), 2)

        # Add the text "DVD" to the logo
        font = pygame.font.Font(None, 36)
        text = font.render('DVD', True, (255, 255, 255))  # White text
        text_rect = text.get_rect(center=(self.logo_x + self.logo_width // 2, self.logo_y + self.logo_height // 2))

        self.window.blit(text, text_rect)
