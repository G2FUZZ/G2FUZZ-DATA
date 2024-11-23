import numpy as np
import cv2

# Create a black image
image_data = np.zeros((100, 100, 3), dtype=np.uint8)

# Save the image as a BMP file
cv2.imwrite('./tmp/image_data.bmp', image_data)