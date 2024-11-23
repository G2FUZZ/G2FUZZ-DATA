import numpy as np
from PIL import Image

# Create a transparent PNG image
width, height = 300, 300
transparent_color = (0, 0, 0, 0)  # Transparent background color

image = Image.new('RGBA', (width, height), transparent_color)
image.save('./tmp/transparent_image.png')