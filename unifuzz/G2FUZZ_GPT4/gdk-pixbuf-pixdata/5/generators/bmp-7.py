import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image specifications
width, height = 640, 480
color = (255, 0, 0)  # Red

# Create a new image with RGB mode
image = Image.new("RGB", (width, height), color)

# Save the image with DIB header information
image.save('./tmp/red_image.bmp')

print("BMP file has been saved to ./tmp/red_image.bmp")