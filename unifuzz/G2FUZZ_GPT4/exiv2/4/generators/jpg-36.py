import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a gradient image as the background
width, height = 512, 512
background_array = np.zeros((height, width, 3), dtype=np.uint8)
for y in range(height):
    for x in range(width):
        background_array[y, x] = [x % 256, y % 256, (x + y) % 256] # Modulo to create more vibrant gradients

background_image = Image.fromarray(background_array)

# Create a drawing context
draw = ImageDraw.Draw(background_image, 'RGBA')

# Draw rectangles
draw.rectangle([50, 50, 200, 200], fill=(255, 0, 0, 128), outline=(255, 255, 255, 255))
draw.rectangle([312, 50, 462, 200], fill=(0, 255, 0, 128), outline=(255, 255, 255, 255))

# Draw circles (ellipses with equal width and height)
draw.ellipse([50, 312, 200, 462], fill=(0, 0, 255, 128), outline=(255, 255, 255, 255))
draw.ellipse([312, 312, 462, 462], fill=(255, 255, 0, 128), outline=(255, 255, 255, 255))

# Add text annotations
try:
    # Attempt to use a default font
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    # Fall back to a simple font if the preferred font is unavailable
    font = ImageFont.load_default()

draw.text((60, 60), "Red Square", (255, 255, 255), font=font)
draw.text((322, 60), "Green Square", (255, 255, 255), font=font)
draw.text((60, 322), "Blue Circle", (255, 255, 255), font=font)
draw.text((322, 322), "Yellow Circle", (255, 255, 255), font=font)

# Save the original complex image
background_image.save('./tmp/complex_image.jpg', quality=95)

# Demonstrating "compression" by reducing quality
background_path_compressed = './tmp/complex_image_compressed.jpg'
background_image.save(background_path_compressed, quality=10)

print("Complex image saved in ./tmp/: 'complex_image.jpg' (less compression) and 'complex_image_compressed.jpg' (more compression)")