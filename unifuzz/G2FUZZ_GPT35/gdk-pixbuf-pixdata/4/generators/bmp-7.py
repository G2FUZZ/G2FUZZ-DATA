import numpy as np
from PIL import Image

# Create a 32-bit RGBA image with transparency
img = Image.new('RGBA', (100, 100), (0, 0, 255, 128))

# Save the image as a BMP file
img.save('./tmp/transparent_image.bmp')