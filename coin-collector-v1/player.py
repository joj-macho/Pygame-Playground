import pygame
from pygame.locals import *
from pathlib import Path

# Player Animation Settings
NUM_DIRECTIONS = 8  # Number of rows in the sprite sheet for different directions
NUM_FRAMES_PER_DIRECTION = 4  # Number of frames per direction
SCALE_FACTOR = 2  # Scaling factor for the player's sprite.
PLAYER_SPEED = 6  # Number of pixels to move the player

# Image Paths
BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + '/images'
SPRITE_SHEET_PATH = f'{IMAGE_PATH}/Civilian1(black)_Move.png'


class Player(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        '''Initialize the player sprite.'''
        super().__init__()

        # Window dimensions
        self.window_width = window_width
        self.window_height = window_height

        # Animation settings
        self.num_directions = NUM_DIRECTIONS
        self.num_frames_per_direction = NUM_FRAMES_PER_DIRECTION
        self.scale_factor = SCALE_FACTOR
        self.player_speed = PLAYER_SPEED

        # Load the sprite sheet
        self.sprite_sheet = self.load_sprite_sheet(SPRITE_SHEET_PATH, self.num_directions, self.num_frames_per_direction)
        self.image = self.sprite_sheet[0]  # Set initial image

        # Set the initial player position and direction
        self.rect = self.sprite_sheet[0].get_rect()
        self.rect.center = (self.window_width / 2, self.window_height / 2)
        self.direction = 'south'
        
        # Animation-related variables
        self.step_count = 0
        self.step_position = 0
        self.moving = False

        # Apply the scale factor to the player's image
        self.rect.width *= self.scale_factor
        self.rect.height *= self.scale_factor

        # Maximum coordinates to stay within the window
        self.max_width = self.window_width - self.rect.width
        self.max_height = self.window_height - self.rect.height

    def load_sprite_sheet(self, filename, rows, cols):
        '''Load the sprite sheet and extract individual frames.'''
        sprite_sheet = pygame.image.load(filename)
        sprite_width = sprite_sheet.get_width() // cols
        sprite_height = sprite_sheet.get_height() // rows
        sprite_list = []
        for row in range(rows):
            for col in range(cols):
                frame_rect = pygame.Rect(col * sprite_width, row * sprite_height, sprite_width, sprite_height)
                sprite_list.append(sprite_sheet.subsurface(frame_rect))
        return sprite_list

    def update_animation(self):
        '''Update the player's animation based on movement.'''
        if self.moving:
            step_delay = 5
            self.step_count += 1
            if self.step_count >= self.num_frames_per_direction * step_delay:
                self.step_count = 1
            self.step_position = self.step_count // step_delay
        else:
            self.step_count = 0

        direction_order = [
            'south', 'southeast', 'east', 'northeast',
            'north', 'northwest', 'west', 'southwest'
        ]

        frame_index = direction_order.index(self.direction) * self.num_frames_per_direction + self.step_position
        self.image = pygame.transform.scale(self.sprite_sheet[frame_index], (self.rect.width, self.rect.height))

    def update(self):
        '''Update the player's position and animation.'''
        keys_pressed = pygame.key.get_pressed()
        moving_west = keys_pressed[K_LEFT] or keys_pressed[pygame.K_a]
        moving_east = keys_pressed[K_RIGHT] or keys_pressed[pygame.K_d]
        moving_north = keys_pressed[K_UP] or keys_pressed[pygame.K_w]
        moving_south = keys_pressed[K_DOWN] or keys_pressed[pygame.K_s]

        moving_northeast = moving_north and moving_east
        moving_southeast = moving_south and moving_east
        moving_southwest = moving_south and moving_west
        moving_northwest = moving_north and moving_west

        if moving_northeast:
            self.direction = 'northeast'
            self.moving = True
        elif moving_southeast:
            self.direction = 'southeast'
            self.moving = True
        elif moving_southwest:
            self.direction = 'southwest'
            self.moving = True
        elif moving_northwest:
            self.direction = 'northwest'
            self.moving = True
        elif moving_west:
            self.direction = 'west'
            self.moving = True
        elif moving_east:
            self.direction = 'east'
            self.moving = True
        elif moving_north:
            self.direction = 'north'
            self.moving = True
        elif moving_south:
            self.direction = 'south'
            self.moving = True
        else:
            self.moving = False

        if self.moving:
            if 'west' in self.direction or 'northwest' in self.direction or 'southwest' in self.direction:
                self.rect.move_ip(-self.player_speed, 0)
            if 'east' in self.direction or 'northeast' in self.direction or 'southeast' in self.direction:
                self.rect.move_ip(self.player_speed, 0)
            if 'north' in self.direction or 'northwest' in self.direction or 'northeast' in self.direction:
                self.rect.move_ip(0, -self.player_speed)
            if 'south' in self.direction or 'southwest' in self.direction or 'southeast' in self.direction:
                self.rect.move_ip(0, self.player_speed)

            self.rect.y = max(0, min(self.max_height, self.rect.y))
            self.rect.x = max(0, min(self.max_width, self.rect.x))

        self.update_animation()