import os
from PIL import Image

# Create the temp directory if it does not exist
temp_dir = './tmp/'
os.makedirs(temp_dir, exist_ok=True)

def create_ani_file(filename, hotspot=(0, 0)):
    """
    Create a simple .ani file with a defined hotspot.

    Args:
    - filename: The path and name of the file to save.
    - hotspot: A tuple defining the hotspot coordinates.
    """
    # Create a simple 32x32 black image to use as a cursor frame
    img_size = (32, 32)
    image = Image.new("RGBA", img_size, (0, 0, 0, 0))
    
    # Drawing a simple element to visualize the cursor
    for x in range(10, 22):
        for y in range(10, 22):
            image.putpixel((x, y), (255, 255, 255, 255))
    
    # For simplicity, we're saving the frame as a .png file. This is not a real .ani file,
    # but serves as a demonstration since actual .ani file creation requires a more complex approach.
    frame_filename = os.path.join(temp_dir, 'frame.png')
    image.save(frame_filename)

    # Normally, here you would create an .ani file with the frame and hotspot definition.
    # Since Python doesn't have built-in support for creating .ani files, we're simulating the process.
    ani_content = f"ANI File Simulation\nHotspot: {hotspot}\nFrame: {frame_filename}"

    # Save the simulated .ani content to a file
    with open(os.path.join(temp_dir, filename), 'w') as f:
        f.write(ani_content)

# Example usage
create_ani_file('example.ani', hotspot=(16, 16))