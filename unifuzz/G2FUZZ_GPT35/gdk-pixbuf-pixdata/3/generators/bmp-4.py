import numpy as np
import cv2

# Define the image size
width = 300
height = 200

# Create a 24-bit BMP image
img_24bit = np.zeros((height, width, 3), np.uint8)
img_24bit[:, :width//3] = [255, 0, 0]      # Blue
img_24bit[:, width//3:2*width//3] = [0, 255, 0]  # Green
img_24bit[:, 2*width//3:] = [0, 0, 255]     # Red

# Save the 24-bit BMP image
cv2.imwrite('./tmp/24bit.bmp', img_24bit)

# Create a 8-bit BMP image
img_8bit = np.zeros((height, width), np.uint8)
for i in range(width):
    img_8bit[:, i] = i % 256

# Save the 8-bit BMP image
cv2.imwrite('./tmp/8bit.bmp', img_8bit)

# Create a 1-bit BMP image
img_1bit = np.random.randint(0, 2, size=(height, width), dtype=np.uint8) * 255

# Save the 1-bit BMP image
cv2.imwrite('./tmp/1bit.bmp', img_1bit)