from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Define image properties
width, height = 8000, 8000  # High resolution
color = (255, 0, 0)  # A solid color (Red) for simplicity

# Create a new image with RGB mode and the defined color
image = Image.new('RGB', (width, height), color)

# Save the image as a BMP file
image.save('./tmp/large_image.bmp')

print("BMP file has been saved in './tmp/large_image.bmp'")