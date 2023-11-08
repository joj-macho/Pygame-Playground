import pygame
import random

class Target:
    '''Represents a target object for a shooting range game.'''

    def __init__(self, window, window_width, window_height):
        '''
        Initialize the Target instance.

        Parameters:
            window (pygame.Surface): The window to draw into.
            window_width (int): The width of the window.
            window_height (int): The height of the window.
        '''
        # Window Settings
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        # Target Attributes
        self.outer_radius = 25  # Initial target outer radius
        self.inner_radius = self.outer_radius // 2  # Initial target inner radius
        self.max_outer_radius = 50  # Maximum target outer radius
        self.grow_speed = 0.4
        self.shrink_speed = 0.4
        self.expanding = True  # Initially expanding
        self.x = random.randint(self.outer_radius, self.window_width - self.outer_radius)  # Initial x position of the target
        self.y = random.randint(self.outer_radius, self.window_height - self.outer_radius)  # Initial y position of the target
        self.visible = True  # Whether the target is currently visible
        self.hit = False

    def update(self):
        '''Update target size (expand or shrink).'''
        if self.visible:
            if self.expanding:
                self.outer_radius += self.grow_speed
                self.inner_radius = self.outer_radius // 2
                if self.outer_radius >= self.max_outer_radius:
                    self.expanding = False
            else:
                self.outer_radius -= self.shrink_speed
                self.inner_radius = self.outer_radius // 2
                if self.outer_radius <= 0:
                    self.outer_radius = 0
                    self.inner_radius = 0
                    self.visible = False

    def reset_target(self):
        '''Reset target to the initial state (expanding).'''
        self.outer_radius = 0
        self.inner_radius = 0
        self.expanding = True
        self.visible = True

    def draw(self):
        '''Draw the target on the window.'''
        if self.visible:
            x, y = self.x, self.y
            size = self.outer_radius
            WHITE = (255, 255, 255)
            BLACK = (0, 0, 0)

            pygame.draw.circle(self.window, WHITE, (x, y), size)
            pygame.draw.circle(self.window, BLACK, (x, y), size * 0.8)
            pygame.draw.circle(self.window, WHITE, (x, y), size * 0.6)
            pygame.draw.circle(self.window, BLACK, (x, y), size * 0.4)

    def check_hit(self, x, y):
        '''
        Check if the target is hit by a shot.

        Parameters:
            x (int): X-coordinate of the shot.
            y (int): Y-coordinate of the shot.

        Returns:
            bool: True if the target is hit, False otherwise.
        '''
        if not self.hit and (x - self.x) ** 2 + (y - self.y) ** 2 <= self.outer_radius ** 2:
            self.hit = True
            return True
        return False
