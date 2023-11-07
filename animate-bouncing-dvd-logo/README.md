# DVD Logo Animation

## Description

The DVD Logo Animation is a Python program that uses the Pygame library to create an animated simulation of the iconic bouncing DVD logo. The program includes two main variations: `main_dvd_logo.py` for a single DVD logo and `main_n_dvd_logo.py` for multiple DVD logos of different colors bouncing within a window. The animation provides a fun and nostalgic experience reminiscent of the DVD player screensaver.

### Files

- `dvd_logo.py`: Contains the `DVDLogo` class definition, responsible for managing the properties and behavior of the bouncing DVD logo.
- `main_dvd_logo.py`: The main program file for the single DVD logo animation.
- `main_n_dvd_logo.py`: The main program file for the multi-colored DVD logos animation.

## How It Works

The program utilizes the Pygame library to create a graphical window for rendering and animating the DVD logos. Here's how it works:

1. **Initialization**: The `DVDLogo` class is responsible for managing the DVD logo's properties and behavior. In the constructor, it initializes parameters such as the Pygame window, window dimensions, DVD logo dimensions, color, initial position, and random speeds within a specified range.

2. **Animation Loop**: Both `main_dvd_logo.py` and `main_n_dvd_logo.py` contain a common animation loop that manages the Pygame event handling, logo updates, drawing, and rendering. The loop repeats continuously, allowing the logos to bounce around the window.

3. **Bouncing Logic**: The `DVDLogo` class updates the logo's position based on its speed in the `update` method. The logo bounces off the screen edges and specifically, when it hits the boundary of the window, it changes direction and increments a counter to track corner hits.

4. **Drawing**: The `draw` method in the `DVDLogo` class uses Pygame to render the DVD-like logo as an ellipse with the specified color, adds the text "DVD," and draws a border around it. The logo is drawn in its updated position on the Pygame window.

5. **Display**: Pygame continually updates the window display, providing smooth animation. The `main` program files are responsible for handling the event loop, updating the logos, and refreshing the display at a specified frame rate.


## Program Input & Output

There is no direct user input required to run the program. Users can execute `main_dvd_logo.py` or `main_n_dvd_logo.py` to start the DVD logo animation. The animations will run until the user closes the Pygame window.

The output is a graphical display of the DVD logo animation. Depending on the version (single logo or multi-colored logos), users will see one or multiple DVD logos bouncing around a window. The corner hits are displayed as a counter on the window to track how many times the logos hit the corners.


