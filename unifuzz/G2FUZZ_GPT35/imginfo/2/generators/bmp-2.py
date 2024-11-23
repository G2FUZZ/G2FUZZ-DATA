import numpy as np
import cv2

# Create a sample image data
image_data = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Save the image data as a BMP file
cv2.imwrite('./tmp/image_data.bmp', image_data)