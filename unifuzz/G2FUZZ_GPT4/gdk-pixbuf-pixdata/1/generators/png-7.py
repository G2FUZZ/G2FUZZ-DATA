import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Creating a palette-based image
# Define a simple palette: each entry consists of (R, G, B)
palette = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0), # Yellow
    (255, 165, 0), # Orange
    (255, 192, 203), # Pink
    (0, 0, 0), # Black
    (255, 255, 255)  # White
]

# Create an image with an indexed color model
image_size = (100, 100)
image_data = np.zeros((image_size[1], image_size[0]), dtype=np.uint8)

# Generate a simple pattern
for y in range(image_size[1]):
    for x in range(image_size[0]):
        # This example uses a simple pattern to select palette colors
        image_data[y, x] = (x // 12 + y // 12) % len(palette)

# Create a PIL image with mode 'P' for palette-based and assign the colors
image = Image.fromarray(image_data, mode='P')
image.putpalette([color for triple in palette for color in triple])

# Save the image
image_file_path = './tmp/palette_based_image.png'
image.save(image_file_path)

print(f'Palette-based image saved to {image_file_path}')