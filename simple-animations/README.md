# Simple Animations

## Description

"Simple Animations" contains programs that demonstrate basic animation concepts using Pygame.

#### Programs

- [Animate Moving Object](animate_moving_object.py): This program shows a simple animation by moving an object around the screen.
- [Animate Moving Image](animate_moving_image.py): This program shows a simple animation by moving an image around the screen.
- [Animate Falling Snow](animate_falling_snow.py): This program demonstrates an animation of falling snowflakes.

## How it Works

The programs in the "Simple Animations" demonstrate creating basic animations using Pygame. These programs share a common structure:

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
    - To display images on the screen, load them using `pygame.image.load()` function which accepts the path to the image you want to load. 

- **Initialize Variables:**
    - Initialize key variables used in the program:
        - `image_x` and `image_y` sets the initial coordinate of the image.
        - `speed_x` and `speed_y` defines the horizontal and vertical speed of the image.
        - `object_x` and `object_y` set the initial coordinates of the moving object.
        - `object_speed_x` and `object_speed_y` define the speed of the object's movement.
        - `snowflakes` is a list of dictionaries representing individual snowflakes.

- **Enter the main loop:**
    - The main loop runs indefinitely, managing the window's content and refreshing once per screen cycle.

Within the main game loop:

- **Handle Events:**
    - Manage events such as mouse clicks, key presses, and window close requests.
    - Listen for the QUIT event to detect the user clicking the window's close button.
    - Perform necessary cleanup by calling `pygame.quit()` and `sys.exit()` when the program should exit.

- **Handle Game/Program Logic:**
    - Implement the program-specific logic, such as moving an object or animating snowflakes.


- **Update the Display:**
    - Clear the display surface to erase any prior content before drawing new content on the screen.
    - Redraw the screen using `pygame.display.update()` to reduce flickering and ensure that the in-memory image is displayed to the user.

- **Control the Frame Rate:**
    - The frame rate is set to 30 frames per second to regulate updates and achieve smooth rendering.


## Program Input & Output

The primary output is the graphical window with animations or effects specific to each program.



#### Animate Moving Object (`animate_moving_object.py`) Output:

![Animate Moving Object Output](output/animate-object-output.gif)

#### Animate Moving Image (`animate_moving_image.py`) Output:

![Animate Moving Image Output'](output/animate-output.gif)


#### Animate Falling Snow (`animate_falling_snow.py`) Output:

![Animate Falling Snow Output](output/animate-snow-output.gif)
