import pygame
import random
from pathlib import Path


# Bird Animation Settings
BIRD_FLAP_INTERVAL = 10
BIRD_SPEED_MIN = 2
BIRD_SPEED_MAX = 5

# Base Path
BASE_PATH = Path(__file__).resolve().parent

# Image Paths
IMAGE_PATH = str(BASE_PATH) + '/images'
BIRD_UP_IMAGE_PATH = f'{IMAGE_PATH}/bird-up.png'
BIRD_DOWN_IMAGE_PATH = f'{IMAGE_PATH}/bird-down.png'


class Bird:
    def __init__(self, window, window_width, window_height):
        '''
        Initialize the Bird instance.

        Parameters:
            window_width (int): The width of the screen.
            window_height (int): The height of the screen.
        '''
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.load_bird_images()  # Load bird images to get width and height
        self.x = 0
        self.y = random.randint(0, window_height - self.height)
        self.speed = random.randint(BIRD_SPEED_MIN, BIRD_SPEED_MAX)
        self.frame = 0
        self.flap_interval = BIRD_FLAP_INTERVAL

    def load_bird_images(self):
        '''Load bird images and get width and height.'''
        # path_to_bird = str(BASE_PATH) + '/images/'
        self.image_up = pygame.image.load(BIRD_UP_IMAGE_PATH)
        self.image_down = pygame.image.load(BIRD_DOWN_IMAGE_PATH)
        self.width = self.image_up.get_width()  # Get width from the image
        self.height = self.image_up.get_height()  # Get height from the image
        self.image = self.image_up  # Initialize with the "up" image

    def update_animation(self):
        '''Update the bird's animation frames.'''
        self.frame += 1
        if self.frame % self.flap_interval == 0:
            if self.image == self.image_up:
                self.image = self.image_down
            else:
                self.image = self.image_up

    def update_position(self):
        '''Update the bird's position.'''
        self.x += self.speed
        if self.x > self.window_width:
            self.reset_position()

    def reset_position(self):
        '''Reset the bird's position.'''
        self.x = 0
        self.y = random.randrange(self.window_height)

    def draw(self, screen):
        '''Draw the bird on the screen.'''
        self.window.blit(self.image, (self.x, self.y))