import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 256x256 gradient image
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    value = i
    gradient[i, :, :] = [value, value, value]

# Save the image with high compression (low quality)
# Note: The quality parameter in imwrite for JPG format ranges from 0 to 100 (high quality).
# Lower values represent higher compression and therefore more loss in image quality.
cv2.imwrite('./tmp/gradient_low_quality.jpg', gradient, [int(cv2.IMWRITE_JPEG_QUALITY), 10])

print("Image generated and saved with lossy compression.")