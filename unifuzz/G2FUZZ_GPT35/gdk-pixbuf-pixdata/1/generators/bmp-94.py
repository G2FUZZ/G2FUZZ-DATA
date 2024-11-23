import numpy as np
import cv2

# Create a blank white image
image = np.ones((800, 800, 3), np.uint8) * 255

# Add text to the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Hello, BMP!', (100, 400), font, 2, (0, 0, 0), 2, cv2.LINE_AA)

# Draw a rectangle on the image
cv2.rectangle(image, (300, 200), (500, 600), (255, 0, 0), 3)

# Save the image as a BMP file with resolution 800x800
cv2.imwrite('./tmp/complex_high_resolution_image.bmp', image)