import pygame
import random
from pygame.locals import *
from pathlib import Path

# Image Paths
BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + '/images'
COIN_PATH = f'{IMAGE_PATH}/coppercoin1.png'
COIN_PATHS = [
    f'{IMAGE_PATH}/coppercoin1.png',
    f'{IMAGE_PATH}/silvercoin1.png',
    f'{IMAGE_PATH}/goldcoin1.png',
    f'{IMAGE_PATH}/crystalcoin1.png',
    f'{IMAGE_PATH}/blackdarkshadowcoin1.png',
]

class Coin(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        '''Initialize the coin sprite.'''
        super().__init__()

        # Window dimensions
        self.window_width = window_width
        self.window_height = window_height

        # Weights for each coin type based on rarity
        coin_type_weights = {
            'copper': 75,
            'silver': 15,
            'gold': 7,
            'crystal': 2,
            'obsidian': 1
        }

        # Randomly select a coin type with rarity using weighted random selection
        coin_types = list(coin_type_weights.keys())
        self.coin_type = random.choices(coin_types, weights=coin_type_weights.values(), k=1)[0]

        # Get the index of the coin path based on its type.
        coin_path = COIN_PATHS[coin_types.index(self.coin_type)]

        # Load the coin image
        self.image = pygame.image.load(coin_path)

        # Set the initial coin position
        self.rect = self.image.get_rect()
        self.spawn_coin()

        # Initialize the time-to-live (TTL) for the coin
        self.ttl = random.randint(7 * 30, 10 * 30)  # Random time between 7 and 10 seconds (converted to frames)

        # Coin scores
        self.scores = {'copper': 1, 'silver': 5, 'gold': 10, 'crystal': 20, 'obsidian': 50}

    def spawn_coin(self):
        '''Randomly spawn the coin on the screen.'''
        self.rect.x = random.randint(self.rect.width, self.window_width - self.rect.width*1.25)
        self.rect.y = random.randint(self.rect.height, self.window_height - self.rect.height*1.25)

    def update(self):
        '''Update the the time-to-live (TTL) for the coin.'''
        self.ttl -= 1

    def should_remove(self):
        '''Check if the coin should be removed based on the TTL.'''
        return self.ttl <= 0
