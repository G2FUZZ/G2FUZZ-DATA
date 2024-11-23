import numpy as np
import cv2

# Create a 100x100 black image
image = np.zeros((100, 100, 3), dtype=np.uint8)

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Platform Compatibility', (5, 50), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

# Save the image as a bmp file
cv2.imwrite('./tmp/platform_compatibility.bmp', image)