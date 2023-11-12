import pygame
from pygame.locals import *
import sys
import random
from pathlib import Path
from bird import Bird

# Colors
DARK_GRAY = (75, 75, 75)
RED = (255, 0, 0)

# Screen Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Game Settings
FRAMES_PER_SECOND = 30
GAME_DURATION = 20  # 20 seconds

# Base Path
BASE_PATH = Path(__file__).resolve().parent

# Image paths
IMAGE_PATH = str(BASE_PATH) + '/images'
CURSOR_IMAGE_PATH = f'{IMAGE_PATH}/target.png'
BACKGROUND_IMAGE_PATH = f'{IMAGE_PATH}/cloud-background.jpg'


def main():
    '''Main function to play the bird shooting game.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Bird Shooter Game')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Load image assets
    cursor_image = pygame.image.load(CURSOR_IMAGE_PATH)
    background = pygame.image.load(BACKGROUND_IMAGE_PATH)

    # Initialize variables
    birds = []  # Init empty bird storage.
    wins, losses = 0, 0  # Init wins and losses
    start_time = pygame.time.get_ticks()  # Init timer

    # Font for text
    large_font = pygame.font.Font(None, 64)
    font = pygame.font.Font(None, 36)

    # Main loop
    while True:
        for event in pygame.event.get():  # Handle events
            if event.type == QUIT:  # Exit the main loop if the user wants to quit
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                cursor_x, cursor_y = pygame.mouse.get_pos()
                cursor_rect = pygame.Rect(cursor_x, cursor_y, 1, 1)

                for bird in birds:
                    bird_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
                    if bird_rect.colliderect(cursor_rect):
                        wins += 1
                        birds.remove(bird)

        # Create new birds at random intervals
        if random.randint(1, 100) < 5:
            new_bird = Bird(window, WINDOW_WIDTH, WINDOW_HEIGHT)
            birds.append(new_bird)        

        # Update bird positions
        for bird in birds:
            bird.x += bird.speed
            if bird.x > WINDOW_WIDTH:
                losses += 1
        
        # Remove off-screen birds from the list
        off_screen_birds = [bird for bird in birds if bird.x > WINDOW_WIDTH]
        for bird in off_screen_birds:
            birds.remove(bird)

        # Game timer
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000

        # Check game over condition
        if elapsed_time >= GAME_DURATION:
            # Game over screen
            text = large_font.render('Game Over', True, RED)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            window.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(2000)  # Display for 2 seconds
            pygame.quit()
            sys.exit()

        cursor_x, cursor_y = pygame.mouse.get_pos()
        cursor_x -= cursor_image.get_width() // 2 
        cursor_y -= cursor_image.get_height() // 2 

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw background
        window.blit(background, (0, 0))

        # Draw all window elements
        for bird in birds:
            bird.update_animation()
            bird.update_position()
            bird.draw(window)
        window.blit(cursor_image, (cursor_x, cursor_y))

        # Render wins and losses
        wins_text = font.render(f'Birds Shot: {wins}', True, (255, 255, 255))
        losses_text = font.render(f'Birds Escaped: {losses}', True, (255, 255, 255))
        time_text = font.render(f'Time Left: {GAME_DURATION - elapsed_time} seconds', True, (255, 255, 255))

        window.blit(wins_text, (10, 10))
        window.blit(losses_text, (10, 50))
        window.blit(time_text, (10, 90))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()