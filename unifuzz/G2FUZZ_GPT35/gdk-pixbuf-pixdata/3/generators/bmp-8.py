import numpy as np
import cv2

# Create a sample image
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Save the image without RLE compression
cv2.imwrite('./tmp/sample_image.bmp', image)