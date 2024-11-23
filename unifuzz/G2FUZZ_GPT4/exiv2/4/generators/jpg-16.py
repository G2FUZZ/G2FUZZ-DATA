from PIL import Image

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a blank image in RGB color space
image = Image.new('RGB', (100, 100), color=(73, 109, 137))

# Convert the image to YCbCr color space
# JPEG files can utilize this color space for more efficient compression
image_ycbcr = image.convert('YCbCr')

# Save the original RGB image and the converted YCbCr image
image.save('./tmp/rgb_image.jpg', 'JPEG')
image_ycbcr.save('./tmp/ycbcr_image.jpg', 'JPEG')

# Creating a hierarchical storage JPEG
# This involves creating multiple resized versions of the original image and saving them in the same JPEG file.
# Note: The standard PIL library does not support the direct creation of hierarchical JPEGs.
# We simulate this feature by creating a series of downscaled images and saving them as individual files.

# Define the scales for the hierarchical storage - these are the scaling factors
scales = [1, 0.5, 0.25]

# Save a series of downscaled images
for scale in scales:
    # Calculate the new size
    new_size = (int(image.width * scale), int(image.height * scale))
    
    # Resize the image using Image.Resampling.LANCZOS for high-quality downsampling
    resized_image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Save the resized image
    resized_image.save(f'./tmp/hierarchical_image_{scale}.jpg', 'JPEG')

print("RGB image saved to ./tmp/rgb_image.jpg")
print("YCbCr image saved to ./tmp/ycbcr_image.jpg")
print("Hierarchical images saved to ./tmp/ with different scales.")