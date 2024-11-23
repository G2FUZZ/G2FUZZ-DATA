import numpy as np
import cv2

# Create a black image
image = np.zeros((100, 100, 3), dtype=np.uint8)

# Set some pixels to red, green, blue, and white
image[10:30, 10:30] = [0, 0, 255]  # Red
image[40:60, 40:60] = [0, 255, 0]  # Green
image[70:90, 70:90] = [255, 0, 0]  # Blue
image[20:40, 60:80] = [255, 255, 255]  # White

# Save the image as a BMP file
cv2.imwrite('./tmp/test_image.bmp', image)