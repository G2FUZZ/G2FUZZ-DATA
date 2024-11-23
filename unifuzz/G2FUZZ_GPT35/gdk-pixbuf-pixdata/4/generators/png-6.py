import numpy as np
from PIL import Image

# Create RGB image
rgb_data = np.zeros((100, 100, 3), dtype=np.uint8)
rgb_data[:, :50] = [255, 0, 0]  # Red left side
rgb_data[:, 50:] = [0, 0, 255]  # Blue right side
rgb_image = Image.fromarray(rgb_data)
rgb_image.save('./tmp/rgb_image.png')

# Create grayscale image
gray_data = np.zeros((100, 100), dtype=np.uint8)
gray_data[:, :50] = 0  # Black left side
gray_data[:, 50:] = 255  # White right side
gray_image = Image.fromarray(gray_data, mode='L')
gray_image.save('./tmp/gray_image.png')

# Create indexed color image
indexed_data = np.array([[0, 1] * 50] * 50, dtype=np.uint8)
indexed_palette = [255, 0, 0, 0, 0, 255]  # Red and Blue palette
indexed_image = Image.fromarray(indexed_data, mode='P')
indexed_image.putpalette(indexed_palette)
indexed_image.save('./tmp/indexed_image.png')

print("Images saved successfully.")