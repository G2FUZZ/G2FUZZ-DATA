import numpy as np
from PIL import Image, ImageDraw
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a resolution-independent image
def generate_gif(image_size):
    # Create a new image with white background
    img = Image.new('RGB', image_size, 'white')
    draw = ImageDraw.Draw(img)

    # Draw a simple square and circle to demonstrate resolution
    square_size = min(image_size) // 4
    circle_radius = square_size // 2
    draw.rectangle([20, 20, 20 + square_size, 20 + square_size], fill="blue", outline="black")
    draw.ellipse([image_size[0] - 20 - 2*circle_radius, 20, image_size[0] - 20, 20 + 2*circle_radius], fill="red", outline="black")

    # Add text
    draw.text((10, image_size[1] - 30), "Resolution: {}x{}".format(*image_size), fill="black")

    return img

# Generate GIFs at different resolutions
resolutions = [(320, 240), (640, 480), (1280, 960)]

# Create a list to hold the Image frames
frames = []

for resolution in resolutions:
    frame = generate_gif(resolution)
    frames.append(frame)

# Save the frames as a GIF
frames[0].save('./tmp/resolution_independence.gif',
               save_all=True,
               append_images=frames[1:],
               duration=500,
               loop=0)