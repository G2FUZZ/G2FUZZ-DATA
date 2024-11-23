import numpy as np
import cv2

# Create a black image
img = np.zeros((200, 200, 3), dtype=np.uint8)

# Add text to the image
cv2.putText(img, "Complex BMP File with Shapes and Gradients",
            (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

# Draw a rectangle
cv2.rectangle(img, (30, 40), (100, 100), (0, 255, 0), 2)

# Draw a circle
cv2.circle(img, (150, 70), 20, (0, 0, 255), -1)

# Create a gradient background
for i in range(200):
    img[:, i] = [i, 255, 255]

# Save the image as a BMP file
cv2.imwrite('./tmp/complex_bmp_file.bmp', img)