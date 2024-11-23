import numpy as np
from PIL import Image

# Create a new RGBA image with transparency
width, height = 100, 100
transparent_color = (0, 0, 0, 0)  # Transparent black
image = Image.new('RGBA', (width, height), transparent_color)

# Save the image as a BMP file
image.save('./tmp/transparent_image.bmp')