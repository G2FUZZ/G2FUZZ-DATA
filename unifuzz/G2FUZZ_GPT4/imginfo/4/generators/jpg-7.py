from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define the size of the image
width, height = 256, 256

# Generate random values for Y, Cb, and Cr channels
# Y (Luminance) should have a higher value for a brighter image
# Cb and Cr (Chrominance) will have values that define the color
y_channel = np.random.randint(0, 255, (height, width), dtype=np.uint8)
cb_channel = np.random.randint(0, 255, (height, width), dtype=np.uint8)
cr_channel = np.random.randint(0, 255, (height, width), dtype=np.uint8)

# Stack the Y, Cb, and Cr channels
ycbcr_image = np.stack([y_channel, cb_channel, cr_channel], axis=-1)

# Create an Image object from the YCbCr data
img = Image.fromarray(ycbcr_image, 'YCbCr')

# Convert the YCbCr image to RGB before saving, as JPG does not support YCbCr natively
img = img.convert('RGB')

# Save the image
img.save('./tmp/ycbcr_image.jpg')

print("Image saved to ./tmp/ycbcr_image.jpg")