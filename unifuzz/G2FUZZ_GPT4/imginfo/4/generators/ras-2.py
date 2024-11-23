from PIL import Image
import numpy as np
import os

# Ensure tmp directory exists
os.makedirs('./tmp/', exist_ok=True)

# Grayscale image
gray_scale = np.array([[i for i in range(256)] for _ in range(256)], dtype=np.uint8)
gray_image = Image.fromarray(gray_scale)
gray_image.save('./tmp/gray_scale.png')  # Changed to .png

# RGB image
rgb_scale = np.zeros((256, 256, 3), dtype=np.uint8)
rgb_scale[:, :, 0] = np.array([[i for i in range(256)] for _ in range(256)])  # Red channel
rgb_scale[:, :, 1] = np.array([[255-i for i in range(256)] for _ in range(256)])  # Green channel
rgb_scale[:, :, 2] = np.array([[128 for _ in range(256)] for _ in range(256)])  # Blue channel with a constant value
rgb_image = Image.fromarray(rgb_scale, 'RGB')
rgb_image.save('./tmp/rgb_scale.png')  # Changed to .png

# Colormap (Indexed color) image
indexed_color = np.array([[i for i in range(256)] for _ in range(256)], dtype=np.uint8)
palette = []
for i in range(256):
    palette.extend([i, 255-i, 128])  # Similar RGB effect as above but using a palette
indexed_image = Image.fromarray(indexed_color, 'P')
indexed_image.putpalette(palette)
indexed_image.save('./tmp/indexed_color.png')  # Changed to .png