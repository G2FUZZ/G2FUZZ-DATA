from PIL import Image

# Create an RGBA Image of 200x200 pixels
width, height = 200, 200
image = Image.new('RGBA', (width, height))

# Generate a gradient of transparency
for x in range(width):
    for y in range(height):
        # Set opacity decreasing from 255 (fully opaque) to 0 (fully transparent)
        opacity = 255 - int((x / width) * 255)
        # Setting a simple blue color with varying opacity
        image.putpixel((x, y), (0, 0, 255, opacity))

# Ensure the ./tmp/ directory exists
import os
os.makedirs('./tmp/', exist_ok=True)

# Save the image
image_file_path = './tmp/gradient_transparency.png'
image.save(image_file_path)

print(f"Image saved at {image_file_path}")