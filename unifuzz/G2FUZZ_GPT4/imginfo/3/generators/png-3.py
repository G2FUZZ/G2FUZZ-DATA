import numpy as np
import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate and save a PNG file with specified color depth
def generate_png(color_depth):
    if color_depth == 1:
        # 1-bit black and white
        data = np.random.randint(0, 2, (100, 100)) * 255  # Generate random black and white data
        mode = '1'
    elif color_depth == 8:
        # 8-bit grayscale
        data = np.random.randint(0, 256, (100, 100)).astype(np.uint8)  # Generate random grayscale data
        mode = 'L'
    elif color_depth == 24:
        # 24-bit truecolor
        data = np.random.randint(0, 256, (100, 100, 3)).astype(np.uint8)  # Generate random RGB data
        mode = 'RGB'
    elif color_depth == 48:
        # 48-bit truecolor with or without alpha
        data = np.random.randint(0, 65536, (100, 100, 3)).astype(np.uint16)  # Generate random RGB data with higher range
        mode = 'RGB'
    else:
        print(f"Unsupported color depth: {color_depth}")
        return

    # Create an image from the data
    if color_depth == 48:
        # PIL doesn't directly support 48-bit images, so we save it using 16 bits per channel
        img = Image.fromarray(data, mode='I;16')
    else:
        img = Image.fromarray(data, mode=mode)

    # Save the image to a file
    file_name = f'./tmp/image_{color_depth}bit.png'
    img.save(file_name)
    print(f"Generated and saved {file_name}")

# Generate and save images with different color depths
for depth in [1, 8, 24, 48]:
    generate_png(depth)