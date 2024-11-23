import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image
width, height = 200, 200
image = Image.new('RGB', (width, height), 'green')

# Path to save the PNG file
file_path = './tmp/color_managed_image.png'

# Save the image without explicitly setting an ICC profile
image.save(file_path)

print(f"Image saved to {file_path}")