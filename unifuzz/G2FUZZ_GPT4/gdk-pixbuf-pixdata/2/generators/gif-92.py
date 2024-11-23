from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_background(size, cell_size):
    """Create a checkerboard background"""
    background = Image.new('RGB', size, (255, 255, 255))
    draw = ImageDraw.Draw(background)
    for y in range(0, size[1], cell_size * 2):
        for x in range(0, size[0], cell_size * 2):
            draw.rectangle([x, y, x + cell_size, y + cell_size], fill=(173, 216, 230))  # Light blue
            draw.rectangle([x + cell_size, y + cell_size, x + cell_size * 2, y + cell_size * 2], fill=(173, 216, 230))  # Light blue
    return background

# Create a list to hold the frames
frames = []

# Define the size of the image and the background cell size
size = (200, 200)
cell_size = 20

# Create a background
background = create_background(size, cell_size)

# Create 20 frames
for i in range(20):
    # Create a new frame using the background
    frame = background.copy()
    draw = ImageDraw.Draw(frame)
    
    # Draw a red circle that moves across the frame
    draw.ellipse((10 + i * 5, 40, 60 + i * 5, 90), fill=(255, 0, 0))
    
    # Corrected: Draw a green square that moves in the opposite direction
    draw.rectangle([size[0] - 60 - i * 5, 110, size[0] - 10 - i * 5, 160], fill=(0, 255, 0))
    
    # Draw a blue circle that moves vertically
    draw.ellipse((140 - i * 5, 10 + i * 5, 190 - i * 5, 60 + i * 5), fill=(0, 0, 255))
    
    # Add the frame to the list
    frames.append(frame)

# Save the frames as an animated GIF
# Loop=0 for infinite looping
frames[0].save('./tmp/complex_animated_loop.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=100, loop=0)