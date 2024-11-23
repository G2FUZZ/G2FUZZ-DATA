from PIL import Image
import numpy as np
import os

# Ensure the tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 1-bit black and white image
image_1bit = Image.new('1', (100, 100), 0)
image_1bit.save('./tmp/1_bit_black_and_white.png')

# Create an 8-bit grayscale image
width, height = 100, 100
array = np.linspace(0, 255, width*height)
grey_scale = np.reshape(array, (height, width)).astype('uint8')
image_8bit = Image.fromarray(grey_scale, 'L')
image_8bit.save('./tmp/8_bit_grayscale.png')

# Create a 16-bit per channel truecolor image
# We'll create a simple gradient for demonstration purposes
width, height = 100, 100
x = np.linspace(0, 65535, width)
y = np.linspace(0, 65535, height)
xx, yy = np.meshgrid(x, y)
zz = (xx + yy) / 2  # Simple gradient
truecolor_array = np.dstack((zz, zz, zz))  # Stack to simulate RGB channels
truecolor_image = Image.fromarray(truecolor_array.astype('uint16'), 'RGB')
truecolor_image.save('./tmp/16_bit_truecolor.png')