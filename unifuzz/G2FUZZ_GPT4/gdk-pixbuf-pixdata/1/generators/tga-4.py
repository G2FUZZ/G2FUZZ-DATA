import os
from PIL import Image
import numpy as np

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_tga_image(width, height, color, filename):
    """Create a single TGA image with the specified color and save it."""
    # Create an image with RGB channels, plus an alpha channel (RGBA)
    data = np.full((height, width, 4), color, dtype=np.uint8)
    img = Image.fromarray(data, 'RGBA')
    img.save(filename)

def concatenate_files(file_list, output_filename):
    """Concatenate multiple files into one."""
    with open(output_filename, 'wb') as outfile:
        for fname in file_list:
            with open(fname, 'rb') as infile:
                outfile.write(infile.read())

# Parameters for the demonstration images
width, height = 100, 100
colors = [(255, 0, 0, 255), (0, 255, 0, 255), (0, 0, 255, 255)]
filenames = ['./tmp/image_{}.tga'.format(i) for i in range(len(colors))]

# Create and save multiple TGA images
for i, color in enumerate(colors):
    create_tga_image(width, height, color, filenames[i])

# Concatenate these images into one file (demonstrative, not TGA-compliant for multi-image)
concatenated_filename = './tmp/concatenated_images.tga'
concatenate_files(filenames, concatenated_filename)

print(f"Generated {len(colors)} TGA files and concatenated them into '{concatenated_filename}'.")