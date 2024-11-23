import numpy as np
from PIL import Image, ImageDraw
import os

def add_pattern(base_img, pattern_type='lines', color=(255, 0, 0)):
    """
    Add a specific pattern over the base image.
    """
    if pattern_type == 'lines':
        draw = ImageDraw.Draw(base_img)
        for x in range(0, base_img.width, 10):
            draw.line((x, 0, x, base_img.height), fill=color)
    elif pattern_type == 'circles':
        draw = ImageDraw.Draw(base_img)
        radius = 10
        for y in range(radius, base_img.height, radius * 4):
            for x in range(radius, base_img.width, radius * 4):
                draw.ellipse((x-radius, y-radius, x+radius, y+radius), outline=color)
    # You can add more patterns here.
    return base_img

def generate_complex_jpeg():
    # Ensure the ./tmp/ directory exists
    os.makedirs('./tmp/', exist_ok=True)
    
    # Generate an example image with multiple gradients and added patterns
    width, height = 512, 512  # Larger dimensions for more detailed patterns
    base_image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Create a more complex gradient
    for y in range(height):
        for x in range(width):
            base_image[y, x] = [(x * y) // 512, (x + y) // 2, (256 - x) // 2]
    
    pil_img = Image.fromarray(base_image)
    
    # Add multiple patterns to the base image to create complexity
    pil_img = add_pattern(pil_img, pattern_type='lines', color=(255, 255, 255))
    pil_img = add_pattern(pil_img, pattern_type='circles', color=(0, 255, 0))
    
    # Save the image with high compression (low quality) to enhance block-based compression artifacts
    compression_quality = 5  # Even lower value for more pronounced artifacts
    pil_img.save('./tmp/complex_jpeg_block_compression_example.jpg', 'JPEG', quality=compression_quality)

generate_complex_jpeg()