from PIL import Image
import numpy as np
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image size and color depth
width, height = 256, 256
color_depth = 16

# Create an array of shape (height, width, 3) for RGB, 16 bit depth
image_data = np.zeros((height, width, 3), dtype=np.uint16)

# Generate a gradient for each channel
for y in range(height):
    for x in range(width):
        image_data[y, x, 0] = (x * 65535) // width  # Red channel gradient
        image_data[y, x, 1] = (y * 65535) // height  # Green channel gradient
        image_data[y, x, 2] = ((x + y) * 65535) // (width + height)  # Blue channel mix

# Convert the numpy array to a PIL image
image = Image.fromarray(image_data, mode='I;16')

# RTF Description to be added to the TIFF file
rtf_description = r"{\rtf1\ansi{\fonttbl\f0\fswiss Helvetica;}\f0\pard This is an \b example \b0 RTF description in a TIFF file.\par}"

# Add the RTF description as a tag in the TIFF file
image.info['Description'] = rtf_description

# Save the image as a TIFF file
file_path = './tmp/high_color_depth_with_rtf_description.tiff'
image.save(file_path, format='TIFF', description=rtf_description)

print(f"Image saved to {file_path}")