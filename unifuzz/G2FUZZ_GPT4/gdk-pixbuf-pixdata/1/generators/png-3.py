import os
import numpy as np
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Example of creating a PNG with varying color depths

# 1-bit black and white image
image_data_bw = np.zeros((100, 100), dtype=np.uint8)
image_data_bw[::2, ::2] = 1  # Create a checkerboard pattern
image_bw = Image.fromarray(image_data_bw * 255)  # Convert to 0-255 scale
image_bw.save('./tmp/black_and_white.png')

# 8-bit grayscale image
image_data_gray = np.arange(256).reshape((16, 16)).repeat(6, axis=0).repeat(6, axis=1)  # Gradient
image_gray = Image.fromarray(image_data_gray.astype(np.uint8))
image_gray.save('./tmp/grayscale.png')

# 24-bit color image (8 bits per channel)
image_data_rgb = np.zeros((100, 100, 3), dtype=np.uint8)
# Red gradient on the X axis
image_data_rgb[:, :, 0] = np.tile(np.arange(100), (100, 1))
# Green gradient on the Y axis
image_data_rgb[:, :, 1] = np.tile(np.arange(100), (100, 1)).T
# Blue set to 128 constant
image_data_rgb[:, :, 2] = 128
image_rgb = Image.fromarray(image_data_rgb)
image_rgb.save('./tmp/rgb_color.png')

# 48-bit color image (16 bits per channel)
image_data_deep_color = np.zeros((100, 100, 3), dtype=np.uint16)
# Red gradient on the X axis
image_data_deep_color[:, :, 0] = np.tile(np.linspace(0, 65535, 100), (100, 1)).astype(np.uint16)
# Green gradient on the Y axis
image_data_deep_color[:, :, 1] = np.tile(np.linspace(0, 65535, 100), (100, 1)).T.astype(np.uint16)
# Blue set to a constant
image_data_deep_color[:, :, 2] = 32768  # Middle value of 16-bit range
image_deep_color = Image.fromarray(image_data_deep_color, mode='I;16')
image_deep_color.save('./tmp/deep_color.png')