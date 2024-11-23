import numpy as np
from PIL import Image

# Create a transparent image with an alpha channel
width, height = 100, 100
data = np.zeros((height, width, 4), dtype=np.uint8)
data[:, :, :3] = [255, 0, 0]  # RGB color (red)
data[:, :, 3] = 128  # Alpha channel (transparency)

# Create a PIL image from the numpy array
image = Image.fromarray(data, 'RGBA')

# Save the image to a file
image.save('./tmp/transparent_image.bmp')