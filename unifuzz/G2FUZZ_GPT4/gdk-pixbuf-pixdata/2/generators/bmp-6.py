from PIL import Image
import os

# Ensure the ./tmp/ directory exists
output_dir = './tmp/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Image dimensions and colors
width, height = 640, 480
color = (255, 0, 0)  # Red

# Create a new image with RGB channels
image = Image.new('RGB', (width, height), color)

# Save the image as BMP
image.save(f'{output_dir}device_independence.bmp')

print("BMP image created and saved to ./tmp/device_independence.bmp")