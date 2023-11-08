import pygame
from pygame.locals import *
import sys
import random
from target import Target

# Constants
DARK_GRAY = (75, 75, 75)  # Color constant for dark grey color
WHITE = (255, 255, 255)  # Color constant for white
RED = (255, 0, 0)
WINDOW_WIDTH = 800  # Width of the window
WINDOW_HEIGHT = 600  # Height of the window
FRAMES_PER_SECOND = 30  # Frame rate for the game


def main():
    '''Main function to run the Shooting Range Game.'''
    # Initialize Pygame
    pygame.init()

    # Create a window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Shooting Range Game')
    clock = pygame.time.Clock()  # Create a clock object to control frame rate

    # Create an empty list to store targets
    targets = []
    max_targets = 10  # Maximum number of targets on the screen at once
    target_timer = random.randint(5, 50)  # Random initial timer

    # Game variables
    running = True
    start_time = pygame.time.get_ticks()
    hits = 0
    missed = 0 
    time_limit = 20  # 20 seconds
    game_over = False

    font = pygame.font.Font(None, 24)  # Initialize a font for text
    game_over_font = pygame.font.Font(None, 48)

    # Main loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if event.button == 1:  # Left mouse button (shoot)
                    x, y = event.pos
                    hit_target = False
                    for target in targets:
                        if target.check_hit(x, y):
                            hit_target = True
                            hits += 1
                            targets.remove(target)  # Remove the hit target
                            
                    if not hit_target:  # Increment missed only if no target was hit
                        missed += 1  # Increment the missed counter

        # Update game state
        if not game_over:
            current_time = pygame.time.get_ticks()
            elapsed_time = (current_time - start_time) // 1000
            if elapsed_time >= time_limit:
                game_over = True

            # Update the target timer
            target_timer -= 1
            if target_timer <= 0:
                if len(targets) < max_targets:
                    targets.append(Target(window, WINDOW_WIDTH, WINDOW_HEIGHT))
                target_timer = random.randint(5, 50)  # Set a new random timer

            # Update the targets
            for target in targets:
                target.update()
                # Remove targets that have become invisible
                if not target.visible:
                    targets.remove(target)

        # Clear the window
        window.fill(DARK_GRAY)

        # Draw targets
        for target in targets:
            target.draw()

        # Display game information
        time_text = font.render(f'Time: {max(time_limit - elapsed_time, 0)} seconds', True, WHITE)
        hits_text = font.render(f'Hits: {hits}', True, WHITE)
        missed_text = font.render(f'Missed: {missed}', True, WHITE)

        window.blit(time_text, (10, 10))
        window.blit(hits_text, (300, 10))
        window.blit(missed_text, (450, 10))

        if game_over:
            game_over_text = game_over_font.render('Game Over!', True, RED)
            window.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - game_over_text.get_height() // 2))

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(FRAMES_PER_SECOND)


if __name__ == '__main__':
    main()

