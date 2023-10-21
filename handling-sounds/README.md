# Sound Playback

## Description

"Sound Playback" contains a program that demonstrates how to play sound in Pygame.

#### Programs

- [Simple Sound Play](sound_effect.py): This program allows you to play a sound when you press the spacebar.


## How it Works

The "Sound Playback" program showcases how to use Pygame to play sound. This program follows a common structure:

- **Importing the Pygame Framework:**
    - Import `pygame` module and its objects to access various elements.
    - Use `from pygame.locals import *` to import constants for convenient use in the script.
    - Import `sys` to handle script termination using `sys.exit()`.

- **Initialize Pygame:**
    - Initialize Pygame using `pygame.init()`, which prepares the modules for use, including hardware setup.

- **Create a window with specific properties:**
    - Use `pygame.display.set_mode()` to create a display surface (window) with specified dimensions (e.g., 800x600 pixels).
    - This function returns a Surface object representing the display, and it can accept flags and depth parameters for display creation.

- **Load Assets:**
    - To play sounds, load them using `pygame.mixer.Sound()` with the path to the sound file.

- **Initialize Variables:**
    - Initialize variables for the positions and Rects of the player/ball and target:
        - `player_x` and `player_y` set the initial position of the player/ball circle.
        - `target_x` and `target_y` set the initial position of the target circle/image.
        - player_radius and target_radius define the radii of the circles.
        - `collision_count` is a variable to track number of collisions within the loop

- **Enter the main loop:**
    - The main loop runs indefinitely, managing the window's content and refreshing once per screen cycle.

Within the main game loop:

- **Handle Events:**
    - Manage events such as mouse clicks, key presses, and window close requests.
    - Listen for the QUIT event to detect the user clicking the window's close button.
    - Perform necessary cleanup by calling `pygame.quit()` and `sys.exit()` when the program should exit.
    - In this program, the spacebar key press (`K_SPACE`) triggers sound playback.

- **Handle Game/Program Logic:**
    - In response to a spacebar key press, the program plays the loaded sound using the `play()` method of the `pygame.mixer.Sound` object.

- **Update the Display:**
    - Clear the display surface to erase any prior content before drawing new content on the screen.

- **Control the Frame Rate:**
    - The frame rate is set to 30 frames per second to regulate updates and achieve smooth rendering.


## Program Input & Output

The primary output of the program is the graphical window. When you press the spacebar key, the program plays a sound associated with the key press.
