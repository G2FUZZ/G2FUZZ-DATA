import numpy as np
import cv2

# Define image dimensions
height, width = 100, 100

# Create 1-bit BMP image (black and white)
img_bw = np.random.randint(0, 2, (height, width), dtype=np.uint8) * 255
cv2.imwrite('./tmp/bw.bmp', img_bw)

# Create 8-bit BMP image (256 colors)
img_8bit = np.random.randint(0, 256, (height, width), dtype=np.uint8)
cv2.imwrite('./tmp/8bit.bmp', img_8bit)

# Create 24-bit BMP image (true color)
img_rgb = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
cv2.imwrite('./tmp/24bit.bmp', img_rgb)

# Create 32-bit BMP image (true color with alpha channel)
img_rgba = np.random.randint(0, 256, (height, width, 4), dtype=np.uint8)
cv2.imwrite('./tmp/32bit.bmp', img_rgba)