from PIL import Image

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# RGB Color Model
rgb_image = Image.new('RGB', (100, 100), (255, 0, 0))  # Red
rgb_image.save('./tmp/rgb_image.png')

# CMYK Color Model
cmyk_image = Image.new('CMYK', (100, 100), (0, 255, 0, 0))  # Green in CMYK
cmyk_image.save('./tmp/cmyk_image.tif')

# Grayscale Color Model
gray_image = Image.new('L', (100, 100), (128))  # Middle gray
gray_image.save('./tmp/gray_image.png')