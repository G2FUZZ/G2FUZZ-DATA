import numpy as np
import cv2

# Create a blank white image
image = np.ones((100, 100, 3), dtype=np.uint8) * 255

# Save the image as a BMP file
cv2.imwrite('./tmp/blank_image.bmp', image)