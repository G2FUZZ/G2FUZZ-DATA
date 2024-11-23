import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image dimensions
width, height = 256, 256

# Generate an image for 1-bit color depth (monochrome)
# Removed dtype=np.uint8 from np.random.choice and added .astype(np.uint8) to convert the data type
image_1bit = np.random.choice([0, 255], size=(height, width)).astype(np.uint8)
img = Image.fromarray(image_1bit, 'L')
img.save('./tmp/monochrome.bmp')

# Generate an image for 24-bit color depth
image_24bit = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
img = Image.fromarray(image_24bit, 'RGB')
img.save('./tmp/high_color.bmp')

# Generate an image for 32-bit color depth (RGBA)
image_32bit = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)
img = Image.fromarray(image_32bit, 'RGBA')
img.save('./tmp/rgba.bmp')