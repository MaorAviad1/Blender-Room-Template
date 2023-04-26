## Room Floor Plan Script

This Python script uses Blender to generate a floor plan of a room with walls, a door, and windows.

### Usage

To use this script, open Blender and follow these steps:

1.  Open a new Text Editor window
2.  Copy and paste the script into the Text Editor window
3.  Modify the script variables to adjust the dimensions of the room, walls, door, and windows as needed
4.  Click the "Run Script" button or press Alt + P to run the script
5.  The room floor plan, walls, door, and windows should be created in the Blender scene

### Variables

The script uses the following variables to define the dimensions of the room, walls, door, and windows:

-   `room_width`: The width of the room
-   `room_length`: The length of the room
-   `wall_thickness`: The thickness of the walls
-   `window_width`: The width of the windows
-   `window_height`: The height of the windows
-   `door_width`: The width of the door
-   `door_height`: The height of the door

These variables can be modified as needed to adjust the dimensions of the floor plan.

### Materials

The script applies materials to the wall, door, and window objects to give them a white color, light blue color, and blue color respectively. These colors can be adjusted by modifying the RGB values in the `diffuse_color` parameter of the `materials.new` function.

### Limitations

This script generates a 2D floor plan of a room, and does not include any 3D modeling or rendering features. Additionally, the script assumes a flat floor plan and does not account for sloped or angled walls or ceilings.
