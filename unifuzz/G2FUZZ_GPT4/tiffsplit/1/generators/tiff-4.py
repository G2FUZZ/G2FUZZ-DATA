from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Generate an RGB image
rgb_image = Image.new("RGB", (100, 100), (255, 0, 0))  # Red square
rgb_image.save('./tmp/rgb_image.tiff')

# Generate a CMYK image
cmyk_color_space = np.zeros((100, 100, 4), dtype=np.uint8)
cmyk_color_space[:, :, 0] = 255  # High cyan
cmyk_color_space[:, :, 1] = 0    # Low magenta
cmyk_color_space[:, :, 2] = 0    # Low yellow
cmyk_color_space[:, :, 3] = 0    # Low key (black)
cmyk_image = Image.fromarray(cmyk_color_space, 'CMYK')
cmyk_image.save('./tmp/cmyk_image.tiff')

# Generate a Grayscale image
gray_image = Image.new("L", (100, 100), 128)  # Medium gray square
gray_image.save('./tmp/gray_image.tiff')