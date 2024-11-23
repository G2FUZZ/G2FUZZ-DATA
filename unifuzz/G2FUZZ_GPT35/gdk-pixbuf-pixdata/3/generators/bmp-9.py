import numpy as np
from PIL import Image

# Create a 100x100 RGB image
image_rgb = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
image_rgb = Image.fromarray(image_rgb, 'RGB')
image_rgb.save('./tmp/rgb_image.bmp')

# Create a 100x100 RGBA image
image_rgba = np.random.randint(0, 256, (100, 100, 4), dtype=np.uint8)
image_rgba = Image.fromarray(image_rgba, 'RGBA')
image_rgba.save('./tmp/rgba_image.bmp')

# Create a 100x100 grayscale image
image_gray = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
image_gray = Image.fromarray(image_gray, 'L')
image_gray.save('./tmp/gray_image.bmp')