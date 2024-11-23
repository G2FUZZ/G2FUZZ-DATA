import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
os.makedirs(output_dir, exist_ok=True)

# Generate a gradient image
height, width = 256, 256
gradient = np.tile(np.linspace(0, 255, width, dtype=np.uint8), (height, 1))

# Convert gradient to a 3-channel (RGB) image
gradient_rgb = cv2.merge([gradient]*3)

# Save the image with different quality levels to demonstrate lossy compression
for quality in [95, 70, 40, 10]:
    filename = f'gradient_quality_{quality}.jpg'
    filepath = os.path.join(output_dir, filename)
    # Save the image with specified JPEG quality (lossy compression)
    cv2.imwrite(filepath, gradient_rgb, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

print("JPEG files have been generated and saved to ./tmp/ showcasing various levels of lossy compression.")