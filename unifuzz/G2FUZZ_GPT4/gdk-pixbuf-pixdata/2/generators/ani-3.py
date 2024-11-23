import os
from PIL import Image, ImageDraw

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

def create_frame(image_size, bg_color, circle_color, radius, position):
    """Create a single frame for the animated graphic."""
    frame = Image.new('RGBA', image_size, bg_color)
    draw = ImageDraw.Draw(frame)
    draw.ellipse((position[0]-radius, position[1]-radius, position[0]+radius, position[1]+radius), fill=circle_color)
    return frame

def create_ani_file(file_path, frames):
    """Create the .ani file."""
    # In this simple example, we will just save the frames as a GIF to mimic an animation
    # as the .ani format is not natively supported by common Python libraries
    frames[0].save(file_path, save_all=True, append_images=frames[1:], duration=100, loop=0)

def generate_animated_graphics():
    frames = []
    image_size = (100, 100)
    bg_color = (255, 255, 255, 0)  # Transparent background
    circle_color = (255, 0, 0, 255)  # Red
    radius = 20
    
    # Generate frames
    for i in range(10):
        position = (50, 10 + i*8)  # Moving the circle downwards
        frame = create_frame(image_size, bg_color, circle_color, radius, position)
        frames.append(frame)
    
    # Save the animation
    ani_file_path = './tmp/animated_cursor.gif'  # Changed from .ani to .gif
    create_ani_file(ani_file_path, frames)

# Generate the animated graphics
generate_animated_graphics()