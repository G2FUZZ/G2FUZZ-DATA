import numpy as np
from PIL import Image

# Create a 100x100 transparent BMP image
img = Image.new('RGBA', (100, 100), (255, 255, 255, 0))  # White image with alpha channel (fully transparent)

# Save the image
img.save('./tmp/transparent_image.bmp')