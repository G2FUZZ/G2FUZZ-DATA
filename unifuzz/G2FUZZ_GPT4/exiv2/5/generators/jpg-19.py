import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a 256x256 gradient image
width, height = 256, 256
gradient = np.zeros((height, width, 3), dtype=np.uint8)
for i in range(height):
    value = i
    gradient[i, :, :] = [value, value, value]

# Custom quantization tables
# Example of simple quantization table, in practice, these tables are carefully chosen based on the application.
# Note: OpenCV does not directly support setting custom quantization tables for JPEG via high-level functions.
# This example demonstrates how you might approach the problem, but direct support in OpenCV for custom quantization
# tables might be limited or require a workaround, such as modifying the libjpeg settings directly or using another library.
# The following table is just for demonstration and might not be applied as expected without further low-level manipulation.
custom_quantization_table = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
], dtype=np.uint8)

# Save the image with custom quantization table
# As of now, there's no direct parameter in cv2.imwrite() to pass custom quantization tables for JPEG.
# However, you can save the image normally and then use another library or tool that supports custom quantization tables
# to re-encode the image if necessary. The demonstration here is for the saving part.
cv2.imwrite('./tmp/gradient_custom_quantization.jpg', gradient, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

print("Image generated and potentially saved with a custom quantization table.")