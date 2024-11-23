import numpy as np
from PIL import Image

# Create a transparent image with alpha channel
width, height = 100, 100
rgba_data = np.zeros((height, width, 4), dtype=np.uint8)
rgba_data[:,:,3] = 255  # Set alpha channel to fully opaque

img = Image.fromarray(rgba_data, 'RGBA')
img.save('./tmp/transparent_image.bmp')