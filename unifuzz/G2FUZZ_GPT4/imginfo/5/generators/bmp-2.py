import os
from PIL import Image
import numpy as np

def create_bmp_with_color_depths(directory):
    # Ensure the ./tmp/ directory exists
    os.makedirs(directory, exist_ok=True)
    
    color_depths = [1, 4, 8, 16, 24, 32]
    image_size = (100, 100)  # Image size: 100x100 pixels

    for depth in color_depths:
        # Generating a random image for demonstration purposes
        if depth in [1, 4, 8]:
            # For these depths, use 'P' mode (palettized) and generate a random palette
            image = Image.new('P', image_size)
            random_palette = np.random.randint(0, 256, size=(256, 3), dtype=np.uint8).flatten()
            image.putpalette(random_palette)
            # For 1-bit images, ensure only two colors
            if depth == 1:
                image = image.point(lambda p: p > 128 and 255)
            else:
                # Fill image data
                data = np.random.randint(0, 2**depth, size=image_size, dtype=np.uint8)
                image.putdata(data.flatten())
        else:
            # For higher color depths, use 'RGB' or 'RGBA' and generate random colors
            mode = 'RGB' if depth == 24 else 'RGBA'
            data = np.random.randint(0, 256, size=(image_size[0], image_size[1], 3 if mode == 'RGB' else 4), dtype=np.uint8)
            image = Image.fromarray(data, mode)

        # Save the image
        filename = os.path.join(directory, f'random_image_{depth}bit.bmp')
        image.save(filename, 'BMP')

# Generate and save BMP files with various color depths into ./tmp/
create_bmp_with_color_depths('./tmp/')