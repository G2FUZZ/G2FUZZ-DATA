from PIL import Image
import numpy as np
import os

# Ensure ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create an image with a gradient
width, height = 800, 600
image = Image.new('RGB', (width, height))
for x in range(width):
    for y in range(height):
        # Gradient from black to white
        value = int((x / width) * 255)
        image.putpixel((x, y), (value, value, value))

# Save the image with JPEG compression
image_path = './tmp/gradient_image.jpg'
image.save(image_path, 'JPEG', quality=85)  # Adjust quality for more or less compression

print(f"Image saved to {image_path}")