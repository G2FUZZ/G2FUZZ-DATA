import numpy as np
import cv2

# Create a simple 2x2 pixel image for demonstration
image_data = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 0]]
], dtype=np.uint8)

# Save the image as a BMP file
cv2.imwrite('./tmp/generated_image.bmp', image_data)