import numpy as np
from PIL import Image
import os

def generate_jpeg_block_compression_example():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate an example image with noticeable block-based compression artifacts.
    # First, create a simple gradient image as a base.
    width, height = 256, 256
    base_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            base_image[y, x] = [x, y, (x + y) // 2]
    
    # Convert the base image to PIL Image format
    pil_img = Image.fromarray(base_image)
    
    # Save the image with high compression (low quality) to enhance block-based compression artifacts
    compression_quality = 10  # Lower values result in higher compression and more noticeable artifacts
    pil_img.save('./tmp/jpeg_block_compression_example.jpg', 'JPEG', quality=compression_quality)

generate_jpeg_block_compression_example()