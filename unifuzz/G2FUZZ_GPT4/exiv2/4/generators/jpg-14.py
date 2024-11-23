from PIL import Image

# Ensure the ./tmp/ directory exists
import os
if not os.path.exists('./tmp/'):
    os.makedirs('./tmp/')

# Create a blank image in RGB color space
image = Image.new('RGB', (100, 100), color = (73, 109, 137))

# Convert the image to YCbCr color space
# JPEG files can utilize this color space for more efficient compression
image_ycbcr = image.convert('YCbCr')

# For demonstration purposes, we'll save both the original RGB image and the converted YCbCr image
image.save('./tmp/rgb_image.jpg', 'JPEG')
image_ycbcr.save('./tmp/ycbcr_image.jpg', 'JPEG')

print("RGB image saved to ./tmp/rgb_image.jpg")
print("YCbCr image saved to ./tmp/ycbcr_image.jpg")