import numpy as np
import cv2
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Generate an image using numpy
# Creating a simple gradient image for demonstration
width, height = 800, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient effect for the image - simple visualization
for i in range(height):
    color_value = 255 * (i / height)
    image[i, :, :] = [color_value, color_value, color_value]

# Save the image with progressive encoding using OpenCV
output_path = './tmp/progressive_encoded_image.jpg'
cv2.imwrite(output_path, image, [int(cv2.IMWRITE_JPEG_PROGRESSIVE), 1, int(cv2.IMWRITE_JPEG_QUALITY), 95])

print(f"Progressive JPEG image saved at: {output_path}")