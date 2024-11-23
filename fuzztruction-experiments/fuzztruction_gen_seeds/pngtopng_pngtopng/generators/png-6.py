import os
from PIL import Image

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a simple gradient image
width, height = 600, 400
image = Image.new("RGB", (width, height))
for x in range(width):
    for y in range(height):
        image.putpixel((x, y), (int(255 * (x / width)), int(255 * (y / height)), 112))

# Save the image without embedding an ICC profile
image.save('./tmp/gradient_without_icc.png', 'PNG')

print("PNG file saved.")