import numpy as np
import os
from PIL import Image

# Parameters
tile_width, tile_height = 64, 64  # Size of the tiles
image_width, image_height = 256, 256  # Overall image dimensions
output_dir = './tmp/'  # Output directory for the tiles

# Create the output directory if it doesn't already exist
os.makedirs(output_dir, exist_ok=True)

# Generate a simple pattern for demonstration purposes
def generate_pattern(width, height):
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            img[y, x] = [x % 255, y % 255, (x*y) % 255]
    return img

# Generate the entire image
full_image = generate_pattern(image_width, image_height)

# Function to save a tile
def save_tile(tile, row, col):
    filename = os.path.join(output_dir, f"tile_{row}_{col}.pixdata")  # Corrected line
    with open(filename, 'wb') as f:
        np.save(f, tile)

# Split the image into tiles and save each tile
for row in range(0, image_height, tile_height):
    for col in range(0, image_width, tile_width):
        tile = full_image[row:row+tile_height, col:col+tile_width]
        save_tile(tile, row//tile_height, col//tile_width)

print("Tiles generated and saved.")