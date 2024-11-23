import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

def create_frame(frame_number, size=(100, 100), square_size=20):
    """
    Creates a single frame for the GIF.
    """
    # Create a blank image
    image = Image.new('RGB', size, (0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Calculate the square's position
    x = (frame_number * 5) % size[0]
    y = size[1] // 2 - square_size // 2

    # Draw a moving square
    draw.rectangle([x, y, x + square_size, y + square_size], fill=(255, 105, 180))

    return image

# Generate frames
frames = [create_frame(i) for i in range(20)]

# Save the frames as a GIF
frames[0].save('./tmp/fixed_resolution_demo.gif',
               save_all=True, append_images=frames[1:], optimize=False, duration=100, loop=0)