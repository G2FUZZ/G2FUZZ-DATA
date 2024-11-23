import numpy as np
from PIL import Image

# Create a 8-bit grayscale image
gray_image = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
gray_image = Image.fromarray(gray_image, mode='L')
gray_image.save('./tmp/8bit_grayscale.png')

# Create a 24-bit RGB image
rgb_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
rgb_image = Image.fromarray(rgb_image, mode='RGB')
rgb_image.save('./tmp/24bit_rgb.png')

# Create a 48-bit RGB image
rgb_image_48bit = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint16)
rgb_image_48bit = Image.fromarray(rgb_image_48bit, mode='RGB')
rgb_image_48bit.save('./tmp/48bit_rgb.png')