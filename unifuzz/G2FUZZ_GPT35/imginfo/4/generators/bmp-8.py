import numpy as np
import cv2

# Create a 100x100 RGB image
image_rgb = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Save the RGB image as a BMP file
cv2.imwrite('./tmp/rgb_image.bmp', image_rgb)

# Create a 100x100 grayscale image
image_gray = np.random.randint(0, 256, (100, 100), dtype=np.uint8)

# Save the grayscale image as a BMP file
cv2.imwrite('./tmp/gray_image.bmp', image_gray)