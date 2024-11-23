from PIL import Image
import os

# Ensure the ./tmp/ directory exists
os.makedirs('./tmp/', exist_ok=True)

# Create a new image with RGB mode and a size of 100x100
image = Image.new('RGB', (100, 100))

# Create some pixel data, for example a diagonal line
for i in range(100):
    image.putpixel((i, i), (255, 255, 255))  # White color

# Save the image as a PNG file instead
image.save('./tmp/example.png')