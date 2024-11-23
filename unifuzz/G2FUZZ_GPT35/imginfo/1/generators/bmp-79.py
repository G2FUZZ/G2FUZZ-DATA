import numpy as np
import cv2

# Create a new blank image with a different size and color
image = np.ones((200, 200, 3), dtype=np.uint8) * 200

# Draw a rectangle on the image
cv2.rectangle(image, (50, 50), (150, 150), (0, 255, 0), 2)

# Add text to the image
cv2.putText(image, 'Complex BMP File', (30, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# Save the image as a BMP file
cv2.imwrite('./tmp/complex_image.bmp', image)