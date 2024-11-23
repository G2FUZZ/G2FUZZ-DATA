import os
from PIL import Image
import numpy as np

# Create the tmp directory if it doesn't exist
os.makedirs('./tmp/', exist_ok=True)

# Function to generate an image with specified color depth
def generate_image_with_color_depth(depth, file_path):
    # For simplicity, generating a 256x256 image
    width, height = 256, 256
    
    if depth == 1:  # 1-bit black and white
        mode = '1'  # 1-bit pixels, black and white, stored with one pixel per byte
        image = Image.new(mode, (width, height))
        # Create a simple black and white checkerboard pattern
        for y in range(height):
            for x in range(width):
                if (x // 32) % 2 == (y // 32) % 2:
                    image.putpixel((x, y), 1)
                else:
                    image.putpixel((x, y), 0)
                    
    elif depth == 8:  # 8-bit grayscale
        mode = 'L'  # 8-bit pixels, black and white
        image = Image.new(mode, (width, height))
        # Create a gradient from black to white
        for y in range(height):
            for x in range(width):
                image.putpixel((x, y), x % 256)
                
    elif depth == 24:  # 24-bit RGB
        mode = 'RGB'  # 3x8-bit pixels, true color
        image = Image.new(mode, (width, height))
        # Create a gradient of colors
        for y in range(height):
            for x in range(width):
                image.putpixel((x, y), (x % 256, y % 256, (x + y) % 256))
                
    elif depth == 48:  # 48-bit RGB with an additional 16-bit alpha
        mode = 'RGBA'  # 4x16-bit pixels, true color with transparency
        image = Image.new(mode, (width, height))
        # Create a gradient of colors with varying transparency
        for y in range(height):
            for x in range(width):
                image.putpixel((x, y), (x % 256, y % 256, (x + y) % 256, x % 256))
    else:
        raise ValueError("Unsupported color depth")
    
    # Save the image
    image.save(file_path)

# Generate images with different color depths
generate_image_with_color_depth(1, './tmp/1bit_black_white.png')
generate_image_with_color_depth(8, './tmp/8bit_grayscale.png')
generate_image_with_color_depth(24, './tmp/24bit_truecolor.png')
generate_image_with_color_depth(48, './tmp/48bit_truecolor_alpha.png')