import numpy as np
import cv2

# Create a dummy image
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]
image[:, 50:] = [0, 0, 255]

# Save the image as a BMP file
cv2.imwrite('./tmp/generated_image.bmp', image)