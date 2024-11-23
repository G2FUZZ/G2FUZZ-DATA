import numpy as np
import cv2

# Create a sample image
image = np.zeros((100, 100, 3), dtype=np.uint8)
image[:, :50] = [255, 0, 0]  # Left half in red
image[:, 50:] = [0, 255, 0]  # Right half in green

# Save the image with interlacing
cv2.imwrite('./tmp/interlaced_image.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 0, cv2.IMWRITE_PNG_STRATEGY, cv2.IMWRITE_PNG_STRATEGY_DEFAULT])