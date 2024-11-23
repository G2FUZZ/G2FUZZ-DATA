import numpy as np
from skimage.io import imsave
import os

def generate_ras_with_rle_compression():
    # Create a directory to store the files if it doesn't already exist
    output_dir = './tmp/'
    os.makedirs(output_dir, exist_ok=True)

    # Define a sample image size and color depth
    width, height = 256, 256
    color_depth = 3  # RGB

    # Generate a sample image with a gradient effect
    img = np.zeros((height, width, color_depth), dtype=np.uint8)
    for x in range(width):
        for y in range(height):
            img[y, x] = [x % 256, y % 256, (x + y) % 256]

    # Define the output path with a .png extension
    output_path = os.path.join(output_dir, 'sample_compressed.png')

    # Save the image
    imsave(output_path, img)

# Call the function to generate the file
generate_ras_with_rle_compression()