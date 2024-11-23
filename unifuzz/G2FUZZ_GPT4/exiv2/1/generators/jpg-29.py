import numpy as np
import cv2
import os

# Create the ./tmp/ directory if it doesn't exist
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

# Generating an image with High Dynamic Range (HDR) support
# Creating a 256x256 pixels image with 3 channels (RGB), but this time we'll use float32 to simulate a wider dynamic range
width, height = 256, 256
image_hdr = np.zeros((height, width, 3), dtype=np.float32)

# Filling the image with a gradient that simulates HDR by using values beyond the standard 0-255 range
for y in range(height):
    for x in range(width):
        # By scaling the values up, we simulate a higher dynamic range. 
        # HDR images often contain values that represent light intensities beyond standard displays.
        image_hdr[y, x] = [x * 2 % 512, y * 2 % 512, ((x+y) * 2 % 512) / 2]

# Since OpenCV's imwrite function does not directly support writing true HDR images in JPEG format,
# we need to first normalize the HDR image to the standard 0-255 range before saving.
# This step is necessary for visualization but does not truly convey HDR content.
image_hdr_normalized = cv2.normalize(image_hdr, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
image_hdr_normalized = image_hdr_normalized.astype(np.uint8)

# Save the "simulated" HDR image using OpenCV
cv2.imwrite('./tmp/gradient_hdr.jpg', image_hdr_normalized)

# Note: This code demonstrates how to simulate an HDR effect by expanding the dynamic range of the content
# and then normalizing it for display or saving. Actual HDR content creation and display require HDR-compatible
# imaging formats (e.g., OpenEXR) and devices.