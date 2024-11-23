import numpy as np
import cv2

# Create a black image
image = np.zeros((100, 100, 3), dtype=np.uint8)

# Add some white text to the image
cv2.putText(image, "BMP File", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Save the image as a BMP file
cv2.imwrite('./tmp/lossless_bmp_file.bmp', image)