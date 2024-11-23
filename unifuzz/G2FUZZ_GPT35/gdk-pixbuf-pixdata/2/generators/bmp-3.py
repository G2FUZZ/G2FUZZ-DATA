import numpy as np
import cv2

# Create a sample image
height, width = 100, 100
image = np.zeros((height, width, 3), dtype=np.uint8)
image[:, :width//2] = [255, 0, 0]  # Blue color on the left half
image[:, width//2:] = [0, 255, 0]  # Green color on the right half

# Save the image with RLE compression
cv2.imwrite('./tmp/compressed_image.bmp', image, [cv2.IMWRITE_PXM_BINARY, 1])