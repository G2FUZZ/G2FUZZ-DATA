import numpy as np
import cv2

# Create a simple black and white image
image = np.zeros((100, 100), dtype=np.uint8)

# Save the image as a BMP file
cv2.imwrite('./tmp/lossless_bmp.bmp', image)