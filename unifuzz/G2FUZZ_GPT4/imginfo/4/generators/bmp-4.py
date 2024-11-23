import os
from PIL import Image, ImageDraw

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new 8-bit per pixel image for demonstrating RLE compression
width, height = 100, 100
image = Image.new('P', (width, height))

# Create a drawing context
draw = ImageDraw.Draw(image)

# Draw a simple pattern that will benefit from RLE compression
# Here, we're creating vertical stripes
for x in range(0, width, 10):
    color = 255 if (x // 10) % 2 == 0 else 0  # Alternate between black and white
    draw.line((x, 0, x, height), fill=color)

# Save the image with RLE compression
image_path = './tmp/compressed_image.bmp'
image.save(image_path, 'BMP', bits=8)

print(f"Image saved at {image_path}")