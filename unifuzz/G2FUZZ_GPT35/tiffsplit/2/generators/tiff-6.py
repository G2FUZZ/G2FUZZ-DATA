import numpy as np
import cv2

# Create a sample image
height, width = 200, 200
image = np.ones((height, width), np.uint8) * 255

# Save the image as a multipage TIFF file
for i in range(3):
    cv2.imwrite(f'./tmp/multipage_image_{i}.tiff', image)

print("Multiple pages TIFF files were generated successfully.")