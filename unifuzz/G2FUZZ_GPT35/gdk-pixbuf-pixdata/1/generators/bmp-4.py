import numpy as np
import cv2

# Create a blank white image
image = np.ones((800, 800, 3), np.uint8) * 255

# Save the image as a BMP file with resolution 800x800
cv2.imwrite('./tmp/high_resolution_image.bmp', image)