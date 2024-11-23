import numpy as np
import cv2

# Create a transparent image with an alpha channel
height, width = 100, 100
transparent_image = np.zeros((height, width, 4), dtype=np.uint8)
transparent_image[:, :, 3] = 0  # Set alpha channel to 0 for full transparency

# Save the transparent image as a BMP file
cv2.imwrite('./tmp/transparent_image.bmp', transparent_image)