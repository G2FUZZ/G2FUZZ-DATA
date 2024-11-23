import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Function to generate a PNG file with a specified color depth
def generate_png_file(bit_depth, filename):
    # Create an image array with random values
    if bit_depth == 1:
        # For 1-bit images (black and white), use a 2-color palette
        image_data = np.random.randint(0, 2, (100, 100)).astype(np.bool)
        mode = '1'
    elif bit_depth == 8:
        # For 8-bit images (grayscale), generate values between 0 and 255
        image_data = np.random.randint(0, 256, (100, 100)).astype(np.uint8)
        mode = 'L'
    elif bit_depth in [24, 32]:
        # For 24-bit and 32-bit images, generate RGB(A) values
        shape = (100, 100, 3) if bit_depth == 24 else (100, 100, 4)
        image_data = np.random.randint(0, 256, shape).astype(np.uint8)
        mode = 'RGB' if bit_depth == 24 else 'RGBA'
    else:
        raise ValueError("Unsupported bit depth")

    # Convert the numpy array to a PIL Image object
    image = Image.fromarray(image_data, mode=mode)
    
    # Save the image in PNG format
    image.save(f'./tmp/{filename}.png')

# Generate PNG files for each supported color depth
generate_png_file(1, 'image_1bit')
generate_png_file(8, 'image_8bit')
generate_png_file(24, 'image_24bit')
generate_png_file(32, 'image_32bit')