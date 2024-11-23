import numpy as np
import cv2

# Create a black image
height, width = 200, 200
image = np.zeros((height, width, 3), dtype=np.uint8)

# Draw a white rectangle in the middle of the image
start_point = (50, 50)
end_point = (150, 150)
color = (255, 255, 255)
thickness = -1  # Filled rectangle
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Save the image as a BMP file
cv2.imwrite('./tmp/generated_image.bmp', image)