import pygame
from pygame.locals import *
import sys
import random
from player import Player
from food import Food

# Colors
DARK_GRAY = (75, 75, 75)
WHITE = (255, 255, 255)

# Screen Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Game Settings
FRAMES_PER_SECOND = 30
PLAYER_SIZE = 40
FOOD_SIZE = 20


def main():
    '''Main function to run the Block Eater Game.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Block Eater Game (V2)')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Initialize variables
    font = pygame.font.Font(None, 36)  # Font for text
    player = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT, 300, 400, PLAYER_SIZE)  # Initialize the player object
    score = 0  # Initialize the player's score
    foods = []  # Initialize food storage

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Get pressed keys and move player based on keys
        keys_pressed = pygame.key.get_pressed()
        player.move(keys_pressed)
        
        # Food spawning
        if random.randint(0, 42) == 1:
            food = Food(window, WINDOW_WIDTH, WINDOW_HEIGHT, FOOD_SIZE)
            foods.append(food)

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw the player object
        player.draw()

        # Draw and update food items
        for food in foods[:]:
            food.draw()
            food.update()
            if player.rect.colliderect(food.rect):
                score += food.score
                foods.remove(food)
            elif food.should_remove():
                foods.remove(food)

        # Display the score on the screen
        score_text = font.render(f'Score: {score}', True, WHITE)
        window.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
