import pygame
from pygame.locals import *
import sys
import random
from player import Player
from coin import Coin

# Colors
DARK_GRAY = (75, 75, 75)
WHITE = (255, 255, 255)

# Screen Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Game Settings
FRAMES_PER_SECOND = 30


def main():
    '''Main function to run the Coin Collector Game.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Coin Collector Game (V1)')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Create a sprite group for all sprites
    all_sprites = pygame.sprite.Group()
    coins_group = pygame.sprite.Group()  # Create a group for coins/

    # Initialize the player
    player = Player(WINDOW_WIDTH, WINDOW_HEIGHT)
    all_sprites.add(player)

    # Game variables
    score = 0
    font = pygame.font.Font(None, 36)  # Font for text

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Update all sprites
        all_sprites.update()

        # Randomly spawn coins
        if random.randint(0, 100) < 25:  # 5% chance of spawning a new coin per frame
            coin = Coin(WINDOW_WIDTH, WINDOW_HEIGHT)
            coins_group.add(coin)
            all_sprites.add(coin)

        # Check for collisions between player and coin
        collisions = pygame.sprite.spritecollide(player, coins_group, True, pygame.sprite.collide_mask)
        for coin in collisions:
            score += coin.scores[coin.coin_type]
            coin.kill()  # Remove the coin from the group

        # Update TTL for remaining coins
        for coin in coins_group:
            coin.update()
        
        # Remove coins that have reached the end of their TTL
        coins_to_remove = [coin for coin in coins_group if coin.should_remove()]
        for coin in coins_to_remove:
            coin.kill()

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw all sprites
        all_sprites.draw(window)
        coins_group.draw(window)  # Draw the remaining coins

        # Draw the score on the screen
        score_text = font.render(f'Score: {score}', True, WHITE)
        window.blit(score_text, (10, 10))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()
