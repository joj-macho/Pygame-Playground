import pygame
from pygame.locals import *

class SnakeSegment:
    def __init__(self, window, x, y, block_size):
        self.window = window
        self.x = x
        self.y = y
        self.block_size = block_size

        self.color = (0, 255, 0)  # Snake color (green)
        self.speed = 5  # Speed of the snake

        self.rect = pygame.Rect(self.x, self.y, self.block_size, self.block_size)

        # Align with the grid
        self.rect.x = (self.rect.x // self.block_size) * self.block_size
        self.rect.y = (self.rect.y // self.block_size) * self.block_size

        # Set initial movement direction
        self.direction = 'RIGHT'

    def move(self):
        # Move the snake in the current direction
        if self.direction == 'UP':
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 'DOWN':
            self.rect.move_ip(0, self.speed)
        elif self.direction == 'LEFT':
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 'RIGHT':
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)