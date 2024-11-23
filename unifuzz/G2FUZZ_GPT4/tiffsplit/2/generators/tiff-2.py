import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp', exist_ok=True)

# Generate a 256x256 pixels image with a gradient
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient from top to bottom
for y in range(height):
    # Gradient from black to red, green, and blue, respectively
    for x in range(width):
        image[y, x] = [(x*255)//width, (y*255)//height, ((x+y)*255)//(width+height)]

# Convert to PIL Image and save as TIFF with high precision (24-bit color)
img = Image.fromarray(image, 'RGB')
img.save('./tmp/high_precision_color.tiff', 'TIFF')

print("TIFF file with high precision color saved.")