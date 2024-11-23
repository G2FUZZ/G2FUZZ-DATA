import numpy as np
import tifffile as tiff
import os

def create_image(width, height, pattern='gradient', channel_mode='RGBA'):
    """
    Create an image based on the specified pattern and channel mode.

    :param width: Width of the image
    :param height: Height of the image
    :param pattern: Pattern type ('gradient', 'stripes', 'checkerboard')
    :param channel_mode: Channel mode ('RGBA', 'RGB')
    :return: NumPy array representing the image
    """
    image = np.zeros((height, width, 4), dtype=np.uint8)  # Always create RGBA, convert to RGB later if needed
    if pattern == 'gradient':
        for x in range(width):
            for y in range(height):
                image[y, x] = [x % 256, y % 256, (x+y) % 256, 255]  # RGBA
    elif pattern == 'stripes':
        for x in range(width):
            for y in range(height):
                if (x // 20) % 2 == 0:
                    image[y, x] = [255, 0, 0, 255]  # Red stripes
                else:
                    image[y, x] = [0, 0, 255, 255]  # Blue stripes
    elif pattern == 'checkerboard':
        for x in range(width):
            for y in range(height):
                if ((x // 20) % 2 == 0 and (y // 20) % 2 == 0) or ((x // 20) % 2 == 1 and (y // 20) % 2 == 1):
                    image[y, x] = [0, 255, 0, 255]  # Green squares
                else:
                    image[y, x] = [255, 255, 0, 255]  # Yellow squares

    if channel_mode == 'RGB':
        image = image[:, :, :3]  # Drop the alpha channel for RGB mode

    return image

# Ensure the ./tmp/ directory exists
output_dir = "./tmp/"
os.makedirs(output_dir, exist_ok=True)

width, height = 256, 256
patterns = ['gradient', 'stripes', 'checkerboard']
modes = ['RGBA', 'RGB']

# Create a multi-page TIFF, each page with different pattern and metadata
with tiff.TiffWriter(os.path.join(output_dir, 'complex_structure.tiff')) as tif:
    for pattern in patterns:
        for mode in modes:
            image = create_image(width, height, pattern=pattern, channel_mode=mode)
            description = f'Pattern: {pattern}, Mode: {mode}'
            metadata = {'Pattern': pattern, 'Mode': mode}
            tif.write(image, description=description, metadata=metadata)

print("Multi-page TIFF file with complex structures has been saved to ./tmp/complex_structure.tiff")