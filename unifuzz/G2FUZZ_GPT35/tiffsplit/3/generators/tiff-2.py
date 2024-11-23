import numpy as np
from PIL import Image

# Create a RGB image
rgb_data = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
rgb_image = Image.fromarray(rgb_data, 'RGB')
rgb_image.save('./tmp/rgb_image.tiff')

# Create a CMYK image
cmyk_data = np.random.randint(0, 255, (300, 300, 4), dtype=np.uint8)
cmyk_image = Image.fromarray(cmyk_data, 'CMYK')
cmyk_image.save('./tmp/cmyk_image.tiff')

# Create a Grayscale image
gray_data = np.random.randint(0, 255, (300, 300), dtype=np.uint8)
gray_image = Image.fromarray(gray_data, 'L')
gray_image.save('./tmp/gray_image.tiff')

# Create an Indexed image
indexed_data = np.random.randint(0, 255, (300, 300), dtype=np.uint8)
indexed_image = Image.fromarray(indexed_data, 'P')
indexed_image.save('./tmp/indexed_image.tiff')