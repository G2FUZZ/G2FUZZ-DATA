import os
from PIL import Image
import numpy as np

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

def create_image(color_depth, file_name):
    # Image size
    width, height = 100, 100
    
    if color_depth == 1:  # 1-bit
        mode = '1'
    elif color_depth == 4:  # 4-bit
        mode = 'P'  # 8-bit pixels, mapped to any other mode using a color palette
        palette = [(i, i, i) for i in range(16)]
    elif color_depth == 8:  # 8-bit
        mode = 'P'  # Using palette mode for demonstration, though it can represent more colors
        palette = [(i, i, i) for i in range(256)]
    elif color_depth == 16:  # 16-bit
        mode = 'I;16'  # 16-bit pixels, unsigned integer
    elif color_depth == 24:  # 24-bit
        mode = 'RGB'
    elif color_depth == 32:  # 32-bit
        mode = 'RGBA'
    else:
        raise ValueError("Unsupported color depth")

    # Create an empty image with the specified mode
    image = Image.new(mode, (width, height))
    
    if color_depth in [4, 8]:
        image.putpalette([val for sublist in palette for val in sublist])
    
    if color_depth in [16, 24, 32]:
        if mode == 'I;16':
            # For 16-bit, generate a grayscale gradient
            array = np.linspace(0, 65535, width * height, dtype=np.uint16).reshape((height, width))
            image = Image.fromarray(array, mode='I;16')
            # Convert to 8-bit grayscale before saving
            image = image.convert('L')
        else:
            # For 24-bit and 32-bit, generate an RGB(A) gradient
            data = np.zeros((height, width, 3 if mode == 'RGB' else 4), dtype=np.uint8)
            for i in range(height):
                for j in range(width):
                    data[i, j] = [i % 256, j % 256, (i+j) % 256] + ([255] if mode == 'RGBA' else [])
            image = Image.fromarray(data, mode=mode)
    else:
        # For lower color depths, draw a simple pattern
        for i in range(height):
            for j in range(width):
                if (i//10 + j//10) % 2 == 0:
                    image.putpixel((j, i), 1 if color_depth == 1 else i % (2**color_depth))

    # Save the image
    image.save(f'./tmp/{file_name}.bmp')

# Create images of various color depths
color_depths = [1, 4, 8, 16, 24, 32]
file_names = ['1bit', '4bit', '8bit', '16bit', '24bit', '32bit']
for depth, name in zip(color_depths, file_names):
    create_image(depth, name)