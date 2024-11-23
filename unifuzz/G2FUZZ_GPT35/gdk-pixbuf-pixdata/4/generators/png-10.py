import numpy as np
import cv2

# Create a blank white image
img = np.ones((100, 100, 3), dtype=np.uint8) * 255

# Add ancillary chunk information
ancillary_info = "Ancillary chunks: PNG files can contain ancillary chunks for storing additional information such as text comments, time stamps, and more."
cv2.putText(img, ancillary_info, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

# Save the image as a png file
cv2.imwrite('./tmp/ancillary_chunk_example.png', img)