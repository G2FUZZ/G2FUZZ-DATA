import numpy as np
import cv2

# Create a black image
height, width = 100, 100
black_image = np.zeros((height, width, 3), np.uint8)

# Save the black image as a BMP file
cv2.imwrite('./tmp/lossless_bmp_file.bmp', black_image)