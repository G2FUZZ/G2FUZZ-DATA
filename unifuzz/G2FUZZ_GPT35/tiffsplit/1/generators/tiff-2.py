import numpy as np
from PIL import Image

# Create an RGB image
rgb_image = Image.new('RGB', (100, 100))
rgb_image.save('./tmp/rgb_image.tiff')

# Create a CMYK image
cmyk_image = Image.new('CMYK', (100, 100))
cmyk_image.save('./tmp/cmyk_image.tiff')

# Create a Grayscale image
gray_image = Image.new('L', (100, 100))
gray_image.save('./tmp/gray_image.tiff')

# Create an Indexed image
indexed_image = Image.new('P', (100, 100))
indexed_image.save('./tmp/indexed_image.tiff')