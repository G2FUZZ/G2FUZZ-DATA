import numpy as np
from PIL import Image

# Create a 100x100 RGB image
rgb_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
rgb_image = Image.fromarray(rgb_image, 'RGB')
rgb_image.save('./tmp/rgb_image.jpg')

# Create a 100x100 YCbCr image
ycbcr_image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
ycbcr_image = Image.fromarray(ycbcr_image, 'YCbCr')
ycbcr_image.save('./tmp/ycbcr_image.jpg')