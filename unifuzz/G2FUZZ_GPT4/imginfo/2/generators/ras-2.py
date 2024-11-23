import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a file with specified color depth
def generate_image(color_depth):
    # Image dimensions
    width, height = 100, 100

    if color_depth == 1:  # 1-bit monochrome
        # Generate a monochrome image (0 or 255)
        data = np.random.choice([0, 255], size=(height, width)).astype('uint8')
    elif color_depth == 8:  # 8-bit grayscale
        # Generate a grayscale image
        data = np.random.randint(0, 256, size=(height, width)).astype('uint8')
    elif color_depth == 24:  # 24-bit truecolor
        # Generate a truecolor image
        data = np.random.randint(0, 256, size=(height, width, 3)).astype('uint8')
    else:
        raise ValueError("Unsupported color depth")

    # Create an image from the numpy array
    image = Image.fromarray(data)

    # Save the image in a widely supported format
    filename = f'./tmp/image_{color_depth}-bit.png'
    image.save(filename)  # PNG format is used by default if no format is specified

# Generate files for different color depths
generate_image(1)  # 1-bit monochrome
generate_image(8)  # 8-bit grayscale
generate_image(24) # 24-bit truecolor