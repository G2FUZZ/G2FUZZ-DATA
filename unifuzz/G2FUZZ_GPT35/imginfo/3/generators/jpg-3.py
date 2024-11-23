import numpy as np
from PIL import Image

# Create a white image with RGB color space
width, height = 100, 100
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255
white_image = Image.fromarray(white_image, 'RGB')
white_image.save('./tmp/white_image.jpg')