import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Image properties
width = 100
height = 100
color = (255, 0, 0)  # Red

# Create a new image with a white background
image = Image.new('RGB', (width, height), color)

# Save the image with a DIB header by saving it as a BMP file
image.save('./tmp/red_square.bmp')

print("BMP file with a DIB header created at './tmp/red_square.bmp'")