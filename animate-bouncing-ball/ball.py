import pygame
import random
from pathlib import Path

class Ball:
    '''
    Class to represent the ball in the animation.
    '''

    def __init__(self, window, window_width, window_height):
        '''
        Initialize the Ball instance.

        Parameters:
            window (pygame.Surface): The window to draw into.
            window_width (int): The width of the window.
            window_height (int): The height of the window.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        # Load ball image asset
        self.load_ball_image()

        # Initialize variables
        self.initialize_position()
        self.initialize_speed()

    def load_ball_image(self):
        '''
        Load the ball image asset.
        '''
        base_path = Path(__file__).resolve().parent
        path_to_ball = str(base_path) + '/images/ball.png'
        self.image = pygame.image.load(path_to_ball)

    def initialize_position(self):
        '''Initialize the position of the ball.'''
        self.max_x = self.window_width - self.image.get_width()
        self.max_y = self.window_height - self.image.get_height()
        self.ball_rect = self.image.get_rect(
            topleft=(random.randint(0, self.max_x), random.randint(0, self.max_y))
        )

    def initialize_speed(self):
        '''Initialize the speed of the ball.'''
        SPEED_OPTIONS = [i for i in range(1, 7)]
        self.speed_x = random.choice(SPEED_OPTIONS)
        self.speed_y = random.choice(SPEED_OPTIONS)

    def update(self):
        '''Update the position of the ball.'''
        # Check for collision with window boundaries and change direction accordingly
        if self.ball_rect.left < 0 or self.ball_rect.right >= self.window_width:
            self.speed_x = -self.speed_x

        if self.ball_rect.top < 0 or self.ball_rect.bottom >= self.window_height:
            self.speed_y = -self.speed_y

        # Update the position based on the speed
        self.ball_rect.left += self.speed_x
        self.ball_rect.top += self.speed_y

    def draw(self):
        '''Draw the ball on the window.'''
        # Blit the ball image onto the window at the current position
        self.window.blit(self.image, self.ball_rect)
