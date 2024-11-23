import numpy as np
import cv2

# Create a black image
img = np.zeros((100, 200, 3), dtype=np.uint8)

# Add text to the image
cv2.putText(img, "Limited Support: BMP files have limited support for advanced features like transparency and layers compared to formats like PNG or TIFF.",
            (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# Save the image as a BMP file
cv2.imwrite('./tmp/limited_support.bmp', img)