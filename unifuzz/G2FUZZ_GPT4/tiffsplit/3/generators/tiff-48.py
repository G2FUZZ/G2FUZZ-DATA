import numpy as np
from PIL import Image, TiffImagePlugin, ImageDraw
import os

# Ensure the ./tmp/ directory exists
directory_path = './tmp/'
os.makedirs(directory_path, exist_ok=True)

# Function to create a gradient image array
def create_gradient_image(width, height, page_number):
    array = np.zeros((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            array[i, j] = [i % 256, j % 256, (i+j) % 256]
            
    # Convert array to image
    img = Image.fromarray(array)
    draw = ImageDraw.Draw(img)
    
    # Draw a simple element that changes with page_number
    draw.text((10, 10), f"Page {page_number}", fill=(255, 255, 255))
    
    return img

# Multi-page TIFF creation with various compression schemes and added metadata
def create_complex_tiff_with_metadata(filename):
    width, height = 256, 256

    # List of compression schemes for demonstration
    compression_schemes = ['tiff_lzw', 'jpeg', 'tiff_adobe_deflate']

    # Create a list of images for a multi-page TIFF file
    images = [create_gradient_image(width, height, i+1) for i, compression in enumerate(compression_schemes)]

    # Save the images as a multi-page TIFF with custom metadata
    images[0].save(filename, save_all=True, append_images=images[1:], compression="tiff_deflate", dpi=(300, 300), metadata={"author": "Author Name", "description": "This is a multi-page TIFF file with custom metadata and different compression schemes."})

# Create a complex TIFF file with metadata
create_complex_tiff_with_metadata('./tmp/complex_sample_with_metadata.tiff')