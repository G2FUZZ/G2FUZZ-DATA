import numpy as np
import cv2
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create an example image, using a 256x256 pixels image with 3 channels (RGB)
# The image will display gradients in all three channels
width, height = 256, 256
image = np.zeros((height, width, 3), dtype=np.uint8)

# Creating a gradient for each channel
for i in range(256):
    image[i, :, 0] = i  # Red channel gradient
    image[:, i, 1] = i  # Green channel gradient
    image[i, :, 2] = 255-i  # Blue channel, inverse gradient

# Define the TIFF file path with JPEG compression
tiff_file_path = os.path.join(output_dir, 'lossy_compressed_image.tiff')

# Save the image with JPEG compression (lossy) inside a TIFF
# Note: OpenCV does not support saving TIFF images with JPEG compression directly.
# However, we can use PIL (Pillow) as an alternative approach to demonstrate the concept.
from PIL import Image
image_pil = Image.fromarray(image)
image_pil.save(tiff_file_path, compression="jpeg", quality=90)  # Adjust quality for more or less compression

print(f"Image saved as {tiff_file_path}")