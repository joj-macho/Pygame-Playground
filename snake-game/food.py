# food.py
import pygame
import random

class Food:
    def __init__(self, window, window_width, window_height, block_size):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.block_size = block_size

        self.color = (255, 0, 0)  # Food color (red)

        self.rect = pygame.Rect(0, 0, self.block_size, self.block_size)
        
        self.spawn_food()

    def spawn_food(self):
        # Align with the grid
        self.rect.x = (self.rect.x // self.block_size) * self.block_size
        self.rect.y = (self.rect.y // self.block_size) * self.block_size

        # Food random position
        self.rect.x = random.randint(0, self.window_width - self.block_size)
        self.rect.y = random.randint(0, self.window_height - self.block_size)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)