import numpy as np
import cv2

# Create a 32-bit RGBA image with transparency
image = np.zeros((100, 100, 4), dtype=np.uint8)
image[:, :, 0] = 255  # Set red channel to maximum
image[:, :, 3] = 128  # Set alpha channel to 50% transparency

# Save the image as a BMP file
cv2.imwrite('./tmp/transparent_image.bmp', image)