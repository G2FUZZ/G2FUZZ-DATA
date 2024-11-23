import numpy as np
import cv2

# Create a 100x100 pixel RGB image (24-bit true color)
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :, 0] = 255  # Set red channel to maximum intensity
image[:, :, 1] = 255  # Set green channel to maximum intensity
image[:, :, 2] = 255  # Set blue channel to maximum intensity

# Save the image as a BMP file
cv2.imwrite('./tmp/true_color.bmp', image)