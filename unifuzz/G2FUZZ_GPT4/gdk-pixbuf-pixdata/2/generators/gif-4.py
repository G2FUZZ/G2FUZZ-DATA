import os
import numpy as np
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_circle_image(diameter, color):
    """
    Generates an image with a circle of a given color and diameter.
    """
    image = Image.new('RGB', (diameter, diameter), 'white')
    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, diameter - 1, diameter - 1), fill=color)
    return image

def generate_gif(output_path, frames, duration=100):
    """
    Generates a GIF from a list of image frames.
    """
    frames[0].save(output_path, save_all=True, append_images=frames[1:], optimize=False, duration=duration, loop=0)

# Parameters for the GIF
frame_count = 10
frame_diameter = 200
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0)]

# Generate frames
frames = [generate_circle_image(frame_diameter, colors[i % len(colors)]) for i in range(frame_count)]

# Generate and save the GIF
gif_path = os.path.join(output_dir, 'example_lossless_compression.gif')
generate_gif(gif_path, frames)

print(f"GIF successfully saved to {gif_path}")